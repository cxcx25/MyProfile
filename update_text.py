import re
import os

new_text = "I empower Managed Service Providers (MSPs) and enterprise teams to achieve scalable growth by optimizing Azure/M365 environments and engineering robust, custom automation solutions. Drawing from deep IT operations and Level 2 support experience, I build tailored tools that streamline complex workflows, reduce ticket volumes, and secure enterprise identities. I am actively seeking remote IAM/Azure roles and am available for freelance automation scripting or Flutter development projects. Let's collaborate to transform your IT service delivery."

for filepath in [
    r'C:\Project\MyProfile\index.html', 
    r'C:\Project\MyProfile\it-modern-theme\index.html',
    r'C:\Project\MyProfile\html5up-dimension\index.html',
    r'C:\Project\MyProfile\original-theme\index.html'
]:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace 'Python & C# Automation' with 'Automation'
    content = content.replace('Python & C# Automation', 'Automation')
    
    # 2. Replace the 'I empower teams...' text
    # The text usually starts with "I empower teams" and ends with "software development."
    pattern = r'I empower teams.*?software development\.'
    content = re.sub(pattern, new_text, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Updated texts globally.')
