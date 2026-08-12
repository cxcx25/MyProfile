import re
import os

new_exp = '''						<!-- Achievements -->
							<article id="one">
								<h2 class="major">Achievements</h2>
								
								<section>
									<a href="#" class="image-achievement"><img src="images/pic01.jpg" alt=""  /></a>
									<h3>L2 IT Operations / MSP Specialist</h3>
									<p><strong>ScalableOS</strong> | May 2026 – Present</p>
									<ul>
										<li>Delivered comprehensive L1/L2 support in a fast-paced MSP environment, troubleshooting hardware (printers, scanners, workstations) and configuring network infrastructure including Cisco Meraki firewalls, access points, and VPNs.</li>
										<li>Administered and secured enterprise Microsoft 365 and Azure environments, leveraging Entra ID, Conditional Access, Intune, and Duo for robust Multi-Factor Authentication (MFA) and unified endpoint management.</li>
										<li>Managed complete Identity and Access Management (IAM) lifecycles for user onboarding/offboarding, securely configuring permissions, distribution groups, and privileged access using Quickpass.</li>
										<li>Utilized RMM (Datto RMM, N-able) and PSA tools to proactively monitor systems, while meticulously maintaining client infrastructure records and knowledge base documentation within IT Glue.</li>
										<li>Acted as a primary technical escalation point for cloud platforms and device security (including Beachhead encryption), maintaining end-to-end ticket ownership to drive rapid issue resolution.</li>
									</ul>
								</section>

								<section>
									<a href="#" class="image-achievement"><img src="images/pic01.jpg" alt=""  /></a>
									<h3>Service Desk Analyst L2 / IAM</h3>
									<p><strong>WeSupport Incorporated</strong> | Feb 2024 – Feb 2026</p>
									<ul>
										<li>Provided Level 2 IAM support for Azure AD (Entra ID), Microsoft 365, and SAP systems using NetIQ Identity Manager.</li>
										<li>Drove automation by developing PowerShell and Python scripts to streamline repetitive service desk and IAM tasks.</li>
									</ul>
								</section>

								<section>
									<a href="#" class="image-achievement"><img src="images/pic02.jpg" alt=""  /></a>
									<h3>At-Home Service Desk T1 Voice</h3>
									<p><strong>TTEC</strong> | Sep 2022 – Feb 2024</p>
									<ul>
										<li>Managed the end-to-end incident lifecycle and provided Tier 1 omnichannel support to diagnose and resolve complex hardware, software, and network incidents, ensuring strict adherence to SLAs and high First Call Resolution (FCR) rates.</li>
										<li>Executed secure user account provisioning and triaged critical Level 2/3 technical escalations to engineering teams with detailed troubleshooting documentation.</li>
									</ul>
								</section>

								<section>
									<a href="#" class="image-achievement"><img src="images/pic03.jpg" alt=""  /></a>
									<h3>Service Desk Specialist</h3>
									<p><strong>Concentrix</strong> | Sep 2021 – Aug 2022</p>
									<ul>
										<li>Functioned as the primary IT support contact to resolve high volumes of hardware, software, and network outages, actively guiding end-users through remote desktop troubleshooting.</li>
										<li>Streamlined incident management workflows and request fulfillment using enterprise ticketing tools, significantly reducing average handle time and improving end-user satisfaction.</li>
									</ul>
								</section>
                                
                                <section>
									<a href="#" class="image-achievement"><img src="images/pic03.jpg" alt=""  /></a>
									<h3>Service Desk</h3>
									<p><strong>TTEC</strong> | Oct 2019 – Aug 2021</p>
									<ul>
										<li>Delivered specialized service desk support in a highly regulated healthcare environment, translating complex technical jargon into actionable troubleshooting steps for non-technical staff.</li>
										<li>Safeguarded sensitive patient records and ensured 100% data accuracy and strict HIPAA compliance during all technical interventions and incident resolutions.</li>
									</ul>
								</section>
							</article>'''

for filepath in [r'C:\Project\MyProfile\html5up-dimension\index.html', r'C:\Project\MyProfile\original-theme\index.html']:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace from <!-- Achievements --> up to <!-- Projects -->
        pattern = r'<!-- Achievements -->\s*<article id="one">.*?</article>\s*'
        content = re.sub(pattern, new_exp + '\n\n\t\t\t\t\t\t', content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
print('Updated html5up-dimension and original-theme')
