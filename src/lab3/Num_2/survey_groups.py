import sys
from dataclasses import dataclass, field
from typing import List, Dict
from collections import defaultdict


@dataclass(order=True)
class Respondent:
    age: int
    full_name: str = field(compare=False)

    def __str__(self):
        return f"{self.full_name} ({self.age})"


@dataclass
class AgeGroup:
    lower: int
    upper: int
    respondents: List[Respondent] = field(default_factory=list)

    def add(self, respondent: Respondent):
        self.respondents.append(respondent)

    def is_in_group(self, age: int) -> bool:
        return self.lower <= age <= self.upper

    def format_label(self) -> str:
        if self.upper == 10**9:
            return f"{self.lower}+"  
        return f"{self.lower}-{self.upper}"

    def get_sorted_respondents(self) -> List[Respondent]:
        return sorted(self.respondents, key=lambda r: (-r.age, r.full_name))


class AgeGroupManager:
    def __init__(self, boundaries: List[int]):
        self.groups: List[AgeGroup] = []
        self._create_groups(boundaries)

    def _create_groups(self, boundaries: List[int]):
        prev = 0
        for bound in sorted(boundaries):
            self.groups.append(AgeGroup(prev, bound))
            prev = bound  # Изменили с bound+1 на просто bound
        self.groups.append(AgeGroup(prev, 10**9))

    def add_respondent(self, respondent: Respondent):
        for group in self.groups:
            if group.is_in_group(respondent.age):
                group.add(respondent)
                return

    def get_non_empty_groups_desc(self) -> List[AgeGroup]:
        return [g for g in reversed(self.groups) if g.respondents]


def main():
    if len(sys.argv) < 2:
        print("Usage: python survey_groups.py <age_boundary_1> <age_boundary_2> ...")
        sys.exit(1)

    boundaries = list(map(int, sys.argv[1:]))

    manager = AgeGroupManager(boundaries)

    for line in sys.stdin:
        line = line.strip()
        if line == "END":
            break
        try:
            full_name, age_str = line.rsplit(",", 1)
            age = int(age_str.strip())
            respondent = Respondent(age, full_name.strip())
            manager.add_respondent(respondent)
        except ValueError:
            print(f"Invalid input line: {line}", file=sys.stderr)

    for group in manager.get_non_empty_groups_desc():
        formatted = ", ".join(str(r) for r in group.get_sorted_respondents())
        print(f"{group.format_label()}: {formatted}")


if __name__ == "__main__":
    main()
