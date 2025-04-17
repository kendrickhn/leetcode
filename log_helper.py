import pandas as pd

def log_problem(id, title, level, solved_by, date, tags):
    path = "leetcode-journal/progress/log.csv"
    df = pd.read_csv(path)
    new_entry = {
        "id": id,
        "title": title,
        "level": level,
        "solved_by": solved_by,
        "date": date,
        "tags": tags
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(path, index=False)
    print(f"✅ Logged: {id} - {title}")
