import os
#import RoboFinder
target = input("enter target: ")
print(" gau is running")
print("\n")
a = os.system(f"echo {target} | gauu | uro | sort -u | anew flinks")
print(" gospider is running")
print("\n")
b = os.system(f"""sudo sh -c \"echo '127.0.0.1 {target}' >> /etc/hosts\"
echo https://{target} | gospider --other-source --include-subs --subs --quiet | uro | sort -u | anew flinks
sudo sed -i '/{target}/d' /etc/hosts """)
print("waybackurl is runing")
print("\n")
c = os.system(f"waybackurls {target} | uro | anew flinks")
print("robofinder is running")
print("\n")
#s = RoboFinder.links()
#for i in s:
 #   h = f"{RoboFinder.url}" + i
  #  os.system(f"echo {h} | anew flinks")
