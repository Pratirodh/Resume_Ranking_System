import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


job_category=["Blockchain developer","Big Data Engineer","Dotnet Engineer","JavaScript","ML Engineer","Python Developer","Sales Engineer","Data Warehouse Manager","Java Developer","Database Administrator","Cloud Computing Engineer","Mern Stack Developer","Information Security Analyst","DevOps Engineer","Cyberintelligence Specialist","IT security Engineer","Software Engineer","Data Analyst","Network Engineer","PHP Developer"]
count=[97,28,34,101,51,111,87,38,43,39,40,37,45,39,28,36,36,80,28,29]
explode = (0, 0, 0, 0, 0, 0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
print(len(job_category),len(count))
print(len(explode))
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(count, labels = job_category,explode=explode,autopct='%1.1f%%')
plt.savefig("pie.jpg")

# show plot
plt.show()
