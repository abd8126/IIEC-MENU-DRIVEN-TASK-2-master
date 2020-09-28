#!/usr/bin/python3 


import cgi
import subprocess as sb

print("content-type: text/html")
print()


a = cgi.FieldStorage()
cmd = a.getvalue("x")

#print(cmd)
if (("run" in cmd) or ("what" in cmd) or ("today's" in cmd) or ("execute" in cmd))and (("date" in cmd)):
    x = sb.getoutput("sudo date")
    print(x)
    sb.getoutput("sudo espeak-ng `date`")
elif (("month" in cmd) or ("what" in cmd) or ("execute" in cmd)or ("today's" in cmd))and (("cal" in cmd) or ("calendar" in cmd)):
    x = sb.getoutput("sudo cal")
    print(x)
    sb.getoutput("sudo espeak-ng `cal`")
elif (("hadoop" in cmd))and (("version" in cmd)):
    x = sb.getoutput("sudo hadoop version")
    print(x)
    sb.getoutput("sudo espeak-ng 'hadoop version'")
elif (("java" in cmd))and (("version" in cmd)):
    x = sb.getoutput("sudo java -version")
    print(x)
    sb.getoutput("sudo espeak-ng 'java version'")
elif (("terraform" in cmd))and (("version" in cmd)):
    x = sb.getoutput("sudo terraform --version")
    print(x)
    sb.getoutput("sudo espeak-ng 'terraform version'")
elif (("docker" in cmd))and (("version" in cmd)):
    x = sb.getoutput("sudo docker version")
    print(x)
    sb.getoutput("sudo espeak-ng 'docker version'")
elif (("python" in cmd))and (("version" in cmd)):
    x = sb.getoutput("sudo python3 -V")
    print(x)
    sb.getoutput("sudo espeak-ng '`python3 -V`'")
elif (("open" in cmd))and (("firefox" in cmd)):
    x = sb.getoutput("sudo espeak-ng 'sorry not supported now'")
    print(x)
elif (("launch" in cmd))and (("docker" in cmd) or ("container" in cmd)):
    x = sb.getoutput("sudo docker run -dit --name os ubuntu ")
    print(x)
    sb.getoutput("sudo espeak-ng 'container launched'")
elif (("show" in cmd) or ("running" in cmd))and (("docker" in cmd) or ("container" in cmd)):
    x = sb.getoutput("sudo docker ps")
    print(x)
    sb.getoutput("sudo espeak-ng 'running container'")
elif (("remove" in cmd) or ("delete" in cmd))and (("docker" in cmd) or ("container" in cmd)):
    x = sb.getoutput("sudo docker rm -f os")
    print(x)
    sb.getoutput("sudo espeak-ng 'container removed'")
elif (("initialize" in cmd) or ("install" in cmd))and (("terraform" in cmd) or ("plugins" in cmd)):
    x = sb.getoutput("sudo terraform init")
    print(x)
    sb.getoutput("sudo espeak-ng 'plugin installed'")
elif (("working" in cmd) or ("track" in cmd))and (("terraform" in cmd) or ("plan" in cmd)):
    x = sb.getoutput("sudo terraform plan")
    print(x)
    sb.getoutput("sudo espeak-ng 'good'")
elif (("validate" in cmd) or ("correct" in cmd))and (("terraform" in cmd) or ("code" in cmd)):
    x = sb.getoutput("sudo terraform validate")
    print(x)
    sb.getoutput("sudo espeak-ng 'successful'")
elif (("run" in cmd) or ("apply" in cmd))and (("terraform" in cmd) or ("code" in cmd)):
    x = sb.getoutput("sudo terraform apply --auto-approve")
    print(x)
    sb.getoutput("sudo espeak-ng 'setup done'")
elif (("delete" in cmd) or ("destroy" in cmd))and (("terraform" in cmd) or ("setup" in cmd)):
    x = sb.getoutput("sudo terraform destroy --auto-approve")
    print(x)
    sb.getoutput("sudo espeak-ng 'setup removed'")
elif (("check" in cmd) or ("send" in cmd))and (("connectivity" in cmd) or ("packets" in cmd) or ("google" in cmd)):
    x = sb.getoutput("sudo ping -c 4 8.8.8.8")
    print(x)
    sb.getoutput("sudo espeak-ng 'yes it is working good'")
else:
    sb.getoutput("sudo espeak-ng 'bye bye have a good day'")
    print("have a good day!!")
    
#x = sb.getoutput(cmd)
    
