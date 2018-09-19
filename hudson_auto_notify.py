#! /usr/bin/env python
#coding=utf-8

import os
import sys
import time
import smtplib
import commands
import linecache
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def get_commiter_email(project):
    commiter_email = list()
    if os.path.exists(ANDROID + project):
        os.chdir(ANDROID + project)
        commands.getstatusoutput('git log -5 --format=format:"%ct^%ce" > MailList.txt') # output format is unix_time^author email
        for line in open(os.getcwd() + "/MailList.txt"):
            commit_time_str = line.split('^')[0]
            print commit_time_str
            if ((NOW - int(commit_time_str)) <= CHECK_HOUR):
                commiter_email.append(line.split('^')[1])
    return commiter_email


BUILD_URL               = sys.argv[1] # jinkens built env BUILD_URL
PROJECT_NAME            = sys.argv[2]
MANIFEST_BRANCH         = sys.argv[3]
ANDROID                 = sys.argv[4] # android src top dir, $HUDSON_BUILDs_ENV/mydroid/android/qiku/
JENKINS_URL             = sys.argv[5] # jinkens built env JENKINS_URL
NOW                     = int(time.time())
CHECK_HOUR              = int(3600 * 6)
sender                  = 'hudson@company.com'
mail_host               = "xx.xxx.x.x"  # smtp host ip
JENKINS_URL_XIAN        = 'http://xx.xxx.xx.206:8080/jenkins/'
JENKINS_URL_SHENZHEN    = 'http://xx.xxx.xx.23:8080/jenkins/'
spm_email_xian          = ['jia@company.com', 'yi@company.com', 'bing@company.com', 'ding@company.com']
spm_email_shenzhen      = ['kate@company.com', 'jack@company.com', 'andy@company.com']

qiku_commiter_email         = get_commiter_email('')
art_commiter_email          = get_commiter_email('art')
bionic_commiter_email       = get_commiter_email('bionic')
edk2_commiter_email         = get_commiter_email('bootable/bootloader/edk2')
lk_commiter_email           = get_commiter_email('bootable/bootloader/lk')
recovery_commiter_email     = get_commiter_email('bootable/recovery')
bsp_commiter_email          = get_commiter_email('bsp')
build_commiter_email        = get_commiter_email('build')
dalvik_commiter_email       = get_commiter_email('dalvik')
development_commiter_email  = get_commiter_email('development')
device_commiter_email       = get_commiter_email('device')
device_360OS_commiter_email = get_commiter_email('device/360OS')
external_commiter_email     = get_commiter_email('external')
frameworks_commiter_email   = get_commiter_email('frameworks')
hardware_commiter_email     = get_commiter_email('hardware')
kernel_commiter_email       = get_commiter_email('kernel')
libcore_commiter_email      = get_commiter_email('libcore')
packages_commiter_email     = get_commiter_email('packages')
prebuilts_commiter_email    = get_commiter_email('prebuilts')
script_commiter_email       = get_commiter_email('script')
system_commiter_email       = get_commiter_email('system')
vendor_commiter_email       = get_commiter_email('vendor')
vendor_360OS_commiter_email = get_commiter_email('vendor/360OS')
gms_commiter_email          = get_commiter_email('vendor/gms')
mm_camera_commiter_email    = get_commiter_email('vendor/qcom/proprietary/mm-camera')
vendor_qiku_commiter_email  = get_commiter_email('vendor/qiku')


# $JENKINS_URL is the env variable powered by jenkins(http://xx.xxx.xx.206:8080/jenkins/env-vars.html/), available to shell scripts
if JENKINS_URL==JENKINS_URL_XIAN :
    Email_All = list(set(spm_email_xian))
elif JENKINS_URL==JENKINS_URL_SHENZHEN:
    Email_All = list(set(spm_email_shenzhen))




subject = "重要"+ "项目编译报错"
Email_Body = "代码编译报错,请SPM通知代码修改者解决" + "<br>项目:" + PROJECT_NAME + "<br>代码分支:" + MANIFEST_BRANCH + "<br>编译任务地址:" + BUILD_URL +" <br>各仓库6小时内代码修改者(最多5个): " \
             + "<br> project android/qiku " + ''.join(qiku_commiter_email) \
             + "<br> project android/qiku/art " + ''.join(art_commiter_email) \
             + "<br> project android/qiku/bionic " + ''.join(bionic_commiter_email) \
             + "<br> project android/qiku/bootable/bootloader/edk2 " + ''.join(edk2_commiter_email) \
             + "<br> project android/qiku/bootable/bootloader/lk " + ''.join(lk_commiter_email) \
             + "<br> project android/qiku/bootable/recovery " + ''.join(recovery_commiter_email) \
             + "<br> project android/qiku/bsp " + ''.join(bsp_commiter_email) \
             + "<br> project android/qiku/build " + ''.join(build_commiter_email) \
             + "<br> project android/qiku/dalvik " + ''.join(dalvik_commiter_email) \
             + "<br> project android/qiku/development " + ''.join(development_commiter_email) \
             + "<br> project android/qiku/device " + ''.join(device_commiter_email) \
             + "<br> project android/qiku/device/360OS " + ''.join(device_360OS_commiter_email) \
             + "<br> project android/qiku/external " + ''.join(external_commiter_email) \
             + "<br> project android/qiku/frameworks " + ''.join(frameworks_commiter_email) \
             + "<br> project android/qiku/hardware " + ''.join(hardware_commiter_email) \
             + "<br> project android/qiku/kernel " + ''.join(kernel_commiter_email) \
             + "<br> project android/qiku/libcore " + ''.join(libcore_commiter_email) \
             + "<br> project android/qiku/packages " + ''.join(packages_commiter_email) \
             + "<br> project android/qiku/prebuilts " + ''.join(prebuilts_commiter_email) \
             + "<br> project android/qiku/script " + ''.join(script_commiter_email) \
             + "<br> project android/qiku/system " + ''.join(system_commiter_email) \
             + "<br> project android/qiku/vendor " + ''.join(vendor_commiter_email) \
             + "<br> project android/qiku/vendor/360OS " + ''.join(vendor_360OS_commiter_email) \
             + "<br> project android/qiku/vendor/gms " + ''.join(gms_commiter_email) \
             + "<br> project android/qiku/vendor/qcom/proprietary/mm-camera " + ''.join(mm_camera_commiter_email) \
             + "<br> project android/qiku/vendor/qiku " + ''.join(vendor_qiku_commiter_email)



message            = MIMEText(Email_Body, 'html', 'utf-8')
message['From']    = Header("hudson@company.com", 'utf-8')
message['To']      = _format_addr('软件代表 <%s>' % ''.join(Email_All))
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.set_debuglevel(1)
    smtpObj.connect(mail_host)
    smtpObj.sendmail(sender, Email_All, message.as_string())
    print ("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException:
    print("\033[31m ERROR:无法发送邮件 \033[0m")
