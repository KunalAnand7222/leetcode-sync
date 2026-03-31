import requests,datetime,random,collections

ku="kunal_codexx"
portfolio="https://kunalportfoliioo.netlify.app/"
ana="https://leetcode.com/graphql"

# ----------- PROFILE -----------
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

# ----------- RECENT SUBMISSIONS -----------
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

today_list=list(today_set)
today_count=len(today_list)

# ----------- SORT WEEKLY DATA -----------
week_sorted=sorted(week_map.items())[-7:]
labels=[str(i[0])[5:] for i in week_sorted]
values=[i[1] for i in week_sorted]

# ----------- PROGRESS % -----------
easy_p=round((easy/total)*100,1) if total else 0
med_p=round((med/total)*100,1) if total else 0
hard_p=round((hard/total)*100,1) if total else 0

# ----------- INTERVIEW SCORE -----------
score=min(100,int((total*0.6)+(med*1.2)+(hard*2)))

# ----------- COMPANY TAGGING (SMART SIMULATION) -----------
companies=["Amazon","Google","Microsoft","Adobe","Flipkart"]
company_tags=random.sample(companies,3)

company_section="\n".join([f"- {c}" for c in company_tags])

# ----------- TODAY LIST -----------
if today_count==0:
    today_section="No problems solved today 🚀"
else:
    today_section="\n".join([f"- {i}" for i in today_list])

# ----------- CHARTS -----------

# Doughnut (colored)
pie_chart=f"https://quickchart.io/chart?c={{type:'doughnut',data:{{labels:['Easy','Medium','Hard'],datasets:[{{data:[{easy},{med},{hard}],backgroundColor:['#22c55e','#facc15','#ef4444']}}]}}}}"

# Weekly chart (green bars)
week_chart=f"https://quickchart.io/chart?c={{type:'bar',data:{{labels:{labels},datasets:[{{label:'Solved',data:{values},backgroundColor:'#22c55e'}}]}}}}"

# ----------- README -----------

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

## 📈 Difficulty Progress
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

## 🎯 Performance
- 🚀 Total Solved: {total}
- 🌍 Global Rank: {ranking}

---

## 🧠 Company Focus
{company_section}

---

## 🏆 Interview Readiness Score
- 💯 Score: {score}/100

---

## 🌐 Connect
- 🔗 Portfolio: {portfolio}
- 📊 LeetCode: https://leetcode.com/u/{ku}/
"""

with open("README.md","w") as f:
    f.write(readme)

# ----------- FORCE COMMIT -----------
with open("activity.txt","w") as f:
    f.write(str(random.randint(1,1000000)))
