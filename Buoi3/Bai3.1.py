students = [
    {"name": "An", "score": 8.5},
    {"name": "Bình", "score": 7.2},
    {"name": "Cường", "score": 4.5},
    {"name": "Đông", "score": 6.0},
    {"name": "Hạnh", "score": 9.0}
]

def getGrade(score):
    if score >= 8.5 :
        return "A"
    elif score >= 7 :
        return "B" 
    elif score >= 5 :
        return "C"
    else :
        return "D"

result = [
    {
        "name" : x.get("name") ,
        "score" : x.get("score"),
        "grade" : getGrade(x.get("score"))
     }
     for x in students
        ]
    


for index, student in enumerate(result,start=1):
    print(f"{index:<5}{student['name']:<12}{student['score']:<10}{student['grade']:<8}")
        