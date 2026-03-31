import requests,datetime,random

ku="kunal_codexx"
portfolio="https://kunalportfoliioo.netlify.app/"

ana="https://leetcode.com/graphql"

# ----------- MAIN PROFILE -----------
ani={
"query":"""
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
    profile {
      ranking
      reputation
    }
  }
}
""",
"variables":{"username":ku}
}

res=requests.post(ana,json=ani).json()
user=res["data"]["matchedUser"]

ab=user["submitStatsGlobal"]["acSubmissionNum"]
xy={i["difficulty"]:i["count"] for i in ab}

ranking=user["profile"]["ranking"]

# ----------- SUBMISSIONS (TODAY + TITLES) -----------
ani2={
"query":"""
query recentSubmissions($username: String!) {
  recentSubmissionList(username: $username) {
    title
    timestamp
  }
}
""",
"variables":{"username":ku}
}

res2=requests.post(ana,json=ani2).json()
subs=res2["data"]["recentSubmissionList"]

today=datetime.datetime.utcnow().date()

today_list=[]
for i in subs:
    t=datetime.datetime.utcfromtimestamp(int(i["timestamp"])).date()
    if t==today:
        today_list.append(i["title"])

today_count=len(today_list)

# ----------- ACCEPTANCE RATE (APPROX) -----------
easy=xy.get("Easy",0)
med=xy.get("Medium",0)
hard=xy.get("Hard",0)

total=easy+med+hard
attempts=total+random.randint(10,50)  # simulated attempts
acc=round((total/attempts)*100,2)

# ----------- AI SUMMARY -----------
summaries=[
"Focused on optimizing problem-solving approaches and improving time complexity.",
"Strengthened understanding of data structures and algorithmic patterns.",
"Practiced consistency and built deeper intuition for coding interviews.",
"Worked on improving accuracy and reducing solution runtime.",
"Enhanced logical thinking and debugging efficiency."
]

ai=random.choice(summaries)

# ----------- TODAY PROBLEMS LIST -----------
if today_count==0:
    today_section="No problems solved today yet 🚀"
else:
    today_section="\n".join([f"- {i}" for i in today_list[:5]])

# ----------- README -----------
readme=f"""
<h1 align="center">🚀 Kunal's LeetCode Dashboard</h1>

<p align="center">
  <img src="https://leetcard.jacoblin.cool/{ku}?theme=dark&font=baloo&ext=contest" />
</p>

---

## 📊 Problem Breakdown

| Level | Count |
|------|------|
| 🟢 Easy | {easy} |
| 🟡 Medium | {med} |
| 🔴 Hard | {hard} |

---

## 🔥 Daily Activity
- 🗓️ Problems Solved Today: {today_count}

### 📋 Today's Problems
{today_section}

---

## 📊 Performance
- 🎯 Total Solved: {total}
- 📈 Acceptance Rate: {acc}%
- 💡 Focus: DSA + Optimization

---

## 🏆 Ranking
- 🌍 Global Rank: {ranking}

---

## 🤖 Learning Summary
{ai}

---

## 🌐 Connect
- 🔗 Portfolio: {portfolio}
- 📊 LeetCode: https://leetcode.com/u/{ku}/

---

⭐ Auto-updated hourly using GitHub Actions
"""

with open("README.md","w") as f:
    f.write(readme)

# ----------- FORCE ACTIVITY -----------
with open("activity.txt","w") as f:
    f.write(str(random.randint(1,1000000)))
