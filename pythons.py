
import sys
import os
import jenkins

print(sys.argv[1])
job_name='param'
s=jenkins.Jenkins('http://localhost:8080/job/param/')
build_info=s.get_build_info(job_name,build_num)
build_info_actions=build_info['actions']
print(build_info_actions)                           


