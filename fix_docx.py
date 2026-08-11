from docx import Document

def fix_docx(docx_path):
    doc = Document(docx_path)
    
    # New professional summary
    new_summary = """Highly experienced IT and Telecommunications Engineer with a strong foundation in enterprise service desk, identity management, and application development. Currently specializing in Identity and Access Management (IAM), providing Level 2 support for Azure AD (Entra ID), Microsoft 365, SAP systems (via NetIQ Identity Manager), and the iqnet IAM platform. Passionate about building practical tools and full-stack solutions, including a C# WPF-based Active Directory and Azure AD management application, a complete Barangay Super App MVP (Go + Flutter + React), and Python-based automation tools using PyQt, SQLite, and Selenium."""
    
    # New Barangay Super App project
    new_project = """Barangay Super App MVP | Full-Stack Community Marketplace | March 2026 – Present

Designed and delivered a complete full-stack Barangay Super App MVP — a production-ready community platform connecting residents for transport services, buy/sell marketplace, messaging, and local services.
Built high-performance Go backend (modular architecture, JWT authentication, RBAC, repository pattern) integrated with PostgreSQL and Docker orchestration.
Developed cross-platform Flutter mobile application (MVVM + GetX) and React admin dashboard with secure role-based access control.
Implemented CI/CD pipelines (GitHub Actions), Verification-Driven Development (VDD), and full security scanning (SAST, SCA, secrets scanning, image scanning) following shift-left principles.
Deployed via Cloudflare Tunnel for live external access; currently 100% MVP integrated and operational."""
    
    # Replace company name from EssilorLuxottica to WeSupport Incorporated
    for para in doc.paragraphs:
        if "EssilorLuxottica" in para.text:
            para.text = para.text.replace("EssilorLuxottica", "WeSupport Incorporated")
        
        # Update professional summary
        if "Highly experienced IT and Telecommunications Engineer" in para.text:
            para.text = new_summary
    
    # Find the Projects section and add the new project
    project_added = False
    for i, para in enumerate(doc.paragraphs):
        if "Project" in para.text and not project_added:
            # Add the new project after this paragraph
            new_para = doc.paragraphs[i + 1].insert_paragraph_before(new_project)
            project_added = True
            break
    
    # Save the updated document
    output_path = r"c:\Project\MyProfile\original-theme\Joseph Rey Marilla_updated.docx"
    doc.save(output_path)
    print(f"Successfully updated {output_path}")

if __name__ == "__main__":
    docx_path = r"c:\Project\MyProfile\original-theme\Joseph Rey Marilla.docx"
    fix_docx(docx_path)
