def work_needed(project_minutes, freelancers):
    hours, minutes = [sum(x) for x in zip(*freelancers)]
    # Shuffle excess minutes into hours
    extra_hours = minutes // 60
    hours += extra_hours
    minutes = minutes % 60
    available_minutes = (hours * 60) + minutes
    if project_minutes <= available_minutes:
        return "Easy Money!"
    else:
        required_minutes = project_minutes - available_minutes
        required_hours = required_minutes // 60
        required_minutes = required_minutes % 60
        return f"I need to work {required_hours} hour(s) and {required_minutes} minute(s)"


def test_work_needed():
    test_cases = [
        (60, [(1,0)], "Easy Money!"),
        (60, [(0,0)], "I need to work 1 hour(s) and 0 minute(s)"),
        (141, [(1,55), (0,25)], "I need to work 0 hour(s) and 1 minute(s)"),
    ]
    for project_minutes, freelancers, outcome in test_cases:
        assert work_needed(project_minutes, freelancers) == outcome
