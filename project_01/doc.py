from docx import Document
from docx.shared import Pt

doc=Document()
doc.add_heading('Sponsorship & Partnership Contact Database',1)
style=doc.styles['Normal']
style.font.name='Calibri'; style.font.size=Pt(10)

def add_company(name,priority,info,contacts):
    doc.add_heading(name,2)
    if priority: doc.add_paragraph(f'Priority: {priority}')
    if info:
        doc.add_heading('General Information',3)
        for k,v in info:
            doc.add_paragraph(f'{k}: {v}',style='List Bullet')
    if contacts:
        doc.add_heading('Potential Contacts',3)
        table=doc.add_table(rows=1,cols=3)
        table.style='Table Grid'
        hdr=table.rows[0].cells
        hdr[0].text='Position'; hdr[1].text='Name'; hdr[2].text='Details'
        for pos,name,det in contacts:
            c=table.add_row().cells
            c[0].text=pos;c[1].text=name;c[2].text=det

add_company("Banque du Caire","Highest probability",
[("Hotline","16990"),("Corporate Phone","+20 2 22646640"),("Website","https://www.bdc.com.eg/bdcwebsite/home.html"),("LinkedIn","https://www.linkedin.com/company/bdcegypt/"),("Instagram","https://www.instagram.com/bdcegypt/"),("Facebook","https://www.facebook.com/BDCEgypt")],
[
("Head of PR","Heba Salman","https://linkedin.com/in/hebasalman"),
("Head of CSR / Sustainable Development","Tamer Tobgy","https://linkedin.com/in/tamertobgy"),
("Head of Corp. Communications","Heidi El-Nahas","LinkedIn + helnahas@bdc.com.eg"),
("Executive Assistant","Sara Hakim","LinkedIn"),
("Head of Sustainability","Omar Elkallini","LinkedIn + Omar.elkallini@bdc.com.eg"),
("Communications & Brand Leader","Hossam Elsawy","LinkedIn, hossam-elsawy@hotmail.com, +201120433755, Connected"),
("Relationship Manager","Youssef Ahmed","LinkedIn"),
("Relationship Manager","Ahmed Raouf","LinkedIn, raoufahmed506@gmail.com"),
("SMEs Strategy Manager","Nada Tawfik","LinkedIn"),
("Senior Relationship Manager","Islam Ibrahim","LinkedIn, islamebrahim1990@gmail.com, Connected"),
("Head of Corporate Marketing","Nayera Helal","LinkedIn, nirooo88@hotmail.com, Connected"),
("Talent Acquisition Manager","Riham Ghoniem","LinkedIn"),
("Talent Acquisition Manager","Mona Abdalgwad","LinkedIn"),
("Talent Acquisition Senior Partner","Habiba El Feky","LinkedIn"),
("Business Development Manager","Patrick Adel","LinkedIn"),
("Debt & Structured Finance RM","Aya Abdel Nasser","LinkedIn, aya1681993@gmail.com, Connected")
])
add_company("CIB","Low (already partnered with GUC)",
[("Hotline","16677"),("Business WhatsApp","+20219666"),("Email","CIB.BusinessContactCenter@cibeg.com"),("Contacts","https://www.cibeg.com/en/contact-us"),("LinkedIn","https://linkedin.com/company/cibegypt"),("Facebook","https://facebook.com/CIBEgypt"),("Instagram","https://instagram.com/cibegypt"),("X","https://x.com/CIB_EG_OFFICIAL")],
[("Partnerships Manager","Hisham Ghazal","LinkedIn"),("Brand Equity Manager","Beshoy William","LinkedIn"),("HR Business Partners Manager","Nourhan Elkholy","LinkedIn")])
add_company("Al Ahli Bank of Kuwait","Medium",[],[
("Head of External Communications","Ahmed Emad","LinkedIn, ahmed.emad10@hotmail.com, Connected"),
("Relationship Manager Supervisor","Ahmed Kozmel","LinkedIn"),
("Corporate Deputy RM","Rawan Hossam","LinkedIn"),
("Relationship Manager","Mahmoud Abdullah","LinkedIn, m.al7amd@hotmail.com"),
("Program Senior Manager","Sarah Attia","LinkedIn"),
("Large Corporate Assistant RM","Farah Wael","LinkedIn")
])
add_company("National Bank of Egypt","Medium",[],[
("Relationship Manager","Mohamed Saber","LinkedIn"),
("Relationship Manager","Hassan Abo Elaref","LinkedIn"),
("Relationship Manager","Mohamed Said","LinkedIn"),
("Relationship Manager","Aliaa Alaa","LinkedIn"),
("Relationship Manager","Mahmoud Maroof","LinkedIn, mahmoudmaroof9@gmail.com"),
("Relationship Manager","Monica Samir","LinkedIn"),
("Relationship Manager","Camellia Emad Saleh","LinkedIn")
])
add_company("Housing & Development Bank","Medium",[],[
("Head of External Communications","Omar Ismaeil","LinkedIn")
])
add_company("Li Auto Egypt","High potential",
[("Website","https://liauto-eg.com/contact-us/"),("Parent Company","https://gb-corporation.com/gb-auto/"),("LinkedIn","https://linkedin.com/company/li-auto-egypt"),("Facebook","https://facebook.com/people/Li-Auto-Egypt/61584177422265/"),("Instagram","https://instagram.com/liautoegypt"),("TikTok","https://tiktok.com/@liautoegypt")],
[("Brand Marketing Manager (GB Corp.)","Allaa Wahdan","LinkedIn"),("Brand Management & Marketing","Nour El Nemr","LinkedIn")])
add_company("Yatta Bakery & Coffee","Local opportunity",
[("Location","Rehab City"),("Owner","+201273000910"),("Business","+201234500084"),("Instagram","https://instagram.com/yatta.eg")],[])
path="C:/Users/Mohand/Documents/fr-innovators/Sponsorship_Partnership_Contact_Data.docx"
doc.save(path)
print(path)
