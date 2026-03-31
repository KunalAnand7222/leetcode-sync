import requests,datetime,random,collections,urllib.parse

ku="kunal_codexx"
portfolio="https://kunalportfoliioo.netlify.app/"
ana="https://leetcode.com/graphql"

# ---------- FETCH PROFILE ----------
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

easy,med,hard=xy.get("Easy",0),xy.get("Medium",0),xy.get("Hard",0)
total=easy+med+hard
ranking=user["profile"]["ranking"]

# ---------- FETCH SUBMISSIONS ----------
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

today_set=set()
week_map=collections.Counter()

for i in subs:
    dt=datetime.datetime.utcfromtimestamp(int(i["timestamp"]))
    d=dt.date()

    if d==today:
        today_set.add(i["title"])

    week_map[d]+=1

today_list=sorted(list(today_set))
today_count=len(today_list)

# ---------- WEEKLY TREND ----------
week_sorted=sorted(week_map.items())[-7:]
labels=[str(i[0])[5:] for i in week_sorted]
values=[i[1] for i in week_sorted]

# ---------- PROGRESS ----------
easy_p=round((easy/total)*100,1) if total else 0
med_p=round((med/total)*100,1) if total else 0
hard_p=round((hard/total)*100,1) if total else 0

# ---------- INTERVIEW SCORE ----------
score=min(100,int((easy*0.5)+(med*1.5)+(hard*3)))

# ---------- CONSISTENCY ----------
active_days=sum(1 for v in values if v>0)

if active_days>=5:
    consistency="🔥 Highly Consistent"
elif active_days>=3:
    consistency="⚡ Improving"
else:
    consistency="📈 Needs Consistency"

# ---------- AI SUMMARY ----------
ai_pool=[
"Improving problem-solving speed and optimizing approaches.",
"Building strong intuition in data structures and algorithms.",
"Focusing on consistency and tackling diverse problem patterns.",
"Enhancing debugging skills and logical thinking.",
"Strengthening concepts for coding interviews."
]

ai=random.choice(ai_pool)

# ---------- TODAY LIST ----------
if today_count==0:
    today_section="No problems solved today 🚀"
else:
    today_section="\n".join([f"- {i}" for i in today_list])

# ---------- CHART CONFIG ----------
pie_config={
"type":"doughnut",
"data":{
"labels":["Easy","Medium","Hard"],
"datasets":[{
"data":[easy,med,hard],
"backgroundColor":["#22c55e","#facc15","#ef4444"]
}]
}
}

week_config={
"type":"bar",
"data":{
"labels":labels,
"datasets":[{
"label":"Solved",
"data":values,
"backgroundColor":"#22c55e"
}]
}
}

pie_chart="https://quickchart.io/chart?c="+urllib.parse.quote(str(pie_config))
week_chart="https://quickchart.io/chart?c="+urllib.parse.quote(str(week_config))

# ---------- README ----------
readme=f"""
<h1 align="center">🚀 Kunal's LeetCode Dashboard</h1>

<p align="center">
  <img src="https://leetcard.jacoblin.cool/{ku}?theme=dark&font=baloo&ext=contest" />
</p>

---

## 📊 Problem Breakdown
<p align="center">
<img src="{pie_chart}" />
</p>

---

## 📈 Difficulty Distribution
- 🟢 Easy: {easy_p}%  
- 🟡 Medium: {med_p}%  
- 🔴 Hard: {hard_p}%  

---

## 🔥 Daily Activity
- 🗓️ Problems Solved Today: {today_count}

### 📋 Today's Problems
{today_section}

---

## 📊 Weekly Progress
<p align="center">
<img src="{week_chart}" />
</p>

---

## ⚡ Consistency Status
{consistency}

---

## 🎯 Performance
- 🚀 Total Solved: {total}
- 🌍 Global Rank: {ranking}
- 💯 Interview Readiness Score: {score}/100

---

## 🤖 Learning Insight
{ai}

---

## 🌐 Connect
- 🔗 Portfolio: {portfolio}
- 📊 LeetCode: https://leetcode.com/u/{ku}/
"""

with open("README.md","w") as f:
    f.write(readme)

# ---------- FORCE COMMIT ----------
with open("activity.txt","w") as f:
    f.write(str(random.randint(1,1000000)))
