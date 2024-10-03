from datetime import datetime

birthdays = {
    "11/10": "Austin",
    "20/10": "Sian",
    "24/11": "Dylan",
    "6/1": "Anda",
    "2/5": "Sarah",
    "16/6": "Kat",
    "20/6": "Josh",
    "23/8": "Anna",
    "12/8": "Kyra",
    "16/9": "Estelle",
}


def get_next_birthday():
    today = datetime.today()

    birthdays_this_year = [
        datetime(int(today.year), int(m), int(d))
        for d, m in [x.split("/") for x in birthdays.keys()]
    ]

    closest_date = min(filter(lambda d: d > today, birthdays_this_year))

    return birthdays[f"{closest_date.day}/{closest_date.month}"], str(
        closest_date.date()
    )


if __name__ == "__main__":
    person, date = get_next_birthday()
    print(f"It is {person}'s birthday next on: {date}")
