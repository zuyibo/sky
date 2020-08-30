
user_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

import requests,re

# 构建请求
web_url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
reps = requests.get(web_url,headers = user_header)

# 解析响应数据
reps.encoding = 'gbk'
# print(reps.text)

# 提取数据
lines = re.findall('<div class="e">(.*?)</div>',reps.text,re.S)
print(lines)

'''
<div class="e">
   <input type="checkbox" name="delivery_jobid" jt="0" class="checkbox" value="124089962" style="display: none;" /> 
   <input type="checkbox" name="delivery_jobid_124089962" jt="0" class="checkbox" value="124089962" style="display: none;" /> 
   <div class="e_icons ick"></div> 
   <a href="https://jobs.51job.com/shanghai-mhq/124089962.html?s=01&amp;t=0" target="_blank" class="el"><p class="t"><span title="自动化测试工程师" class="jname at">自动化测试工程师</span> <span class="time">08-28发布</span> 
     <!----> 
     <!----> 
     <!----> 
     <!----> 
     <!----></p> <p class="info"><span class="sal">1.2-2.4万/月</span> <span class="d at">上海-闵行区 | 3-4年经验 | 本科 | 招若干人</span></p> <p title="五险一金 餐饮补贴 交通补贴 绩效奖金 年终奖金 弹性工作" class="tags"><span><i>五险一金</i><i>餐饮补贴</i><i>交通补贴</i><i>绩效奖金</i><i>年终奖金</i><i>弹性工作</i></span></p></a> 
   <div class="er">
    <a href="https://jobs.51job.com/all/co5736970.html" target="_blank" title="上海比升互联网技术有限公司" class="cname at">上海比升互联网技术有限公司</a> 
    <p class="dc at">合资 | 50-150人</p> 
    <p class="int at">互联网/电子商务</p> 
    <button track-type="searchTrackButtonClick" event-type="99" trace-name="申请职位-职位下" class="p_but">申请职位</button>
   </div>
  </div>
  
  
'''