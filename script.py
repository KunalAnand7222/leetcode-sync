import requests,datetime,random

ku="kunal_codexx"
gh="KunalAnand7222"
portfolio="https://kunalportfoliioo.netlify.app/"

ana="https://leetcode.com/graphql"

# ----------- LEETCODE STATS -----------
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

# ----------- DAILY SUBMISSIONS -----------
ani2={
"query":"""
query recentSubmissions($username: String!) {
  recentSubmissionList(username: $username) {
    timestamp
  }
}
""",
"variables":{"username":ku}
}

res2=requests.post(ana,json=ani2).json()
subs=res2["data"]["recentSubmissionList"]

today=datetime.datetime.utcnow().date()

count=0
for i in subs:
    t=datetime.datetime.utcfromtimestamp(int(i["timestamp"])).date()
    if t==today:
        count+=1

# ----------- AI SUMMARY -----------
summaries=[
"Focused on optimizing problem-solving approaches and improving time complexity.",
"Strengthened understanding of data structures and algorithmic patterns.",
"Practiced consistency and built deeper intuition for coding interviews.",
"Worked on improving accuracy and reducing solution runtime.",
"Enhanced logical thinking and debugging efficiency."
]

ai=random.choice(summaries)

# ----------- README CONTENT -----------
readme=f"""
<h1 align="center">🚀 Kunal's Coding Dashboard</h1>

<p align="center">
  <img src="https://leetcard.jacoblin.cool/{ku}?theme=dark&font=baloo&ext=contest" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={gh}&show_icons=true&theme=radical" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={gh}&theme=react-dark" />
</p>

---

## 📊 LeetCode Breakdown

| Level | Count |
|------|------|
| 🟢 Easy | {xy.get("Easy",0)} |
| 🟡 Medium | {xy.get("Medium",0)} |
| 🔴 Hard | {xy.get("Hard",0)} |

---

## 🔥 Coding Activity
- 🚀 Total Problems Solved: {sum(xy.values())}
- 🗓️ Problems Solved Today: {count}
- 💡 Focus: Data Structures & Algorithms
- ⚡ Consistency Mode: ON

---

## 🏆 Contest & Ranking
- 🌍 Global Rank: {ranking}

---

## 📈 Activity Streak
<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={gh}&theme=radical" />
</p>

---

## 🤖 AI Learning Summary
{ai}

---

## 🌐 Connect With Me
- 🔗 Portfolio: {portfolio}
- 💻 GitHub: https://github.com/{gh}
- 📊 LeetCode: https://leetcode.com/u/{ku}/

---

⭐ Auto-updated every 30 minutes using GitHub Actions
"""

with open("README.md","w") as f:
    f.write(readme)

# ----------- FORCE ACTIVITY -----------
with open("activity.txt","w") as f:
    f.write(str(random.randint(1,1000000)))
