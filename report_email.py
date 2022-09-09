#!/usr/bin/env python3
import os
import datetime

import emails
import reports

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer

styles = getSampleStyleSheet()
info = []
for file in os.listdir("supplier-data/descriptions"):
    with open(f"supplier-data/descriptions/{file}", "r") as f:
        info.append(Spacer(1, 10))
        info.append(Paragraph(f"name: {f.readline().strip()}", styles["BodyText"]))
        info.append(Paragraph(f"weight: {f.readline().strip()}", styles["BodyText"]))
if __name__ == "__main__":
    if "tmp" in os.listdir("."):
        reports.generate_report(os.path.join("tmp", "processed.pdf"),
                                "Processed Update on {}".format(datetime.date.today()), info)
    else:
        os.mkdir("tmp")
        reports.generate_report(os.path.join("tmp", "processed.pdf"),
                                "Processed Update on {}".format(datetime.date.today()), info)
    emails.send(emails.generate("automation@example.com", "student-01-76f692d2e15e@example.com",
                                "Upload Completed - Online Fruit Store",
                                "All fruits are uploaded to our website successfully. A detailed list is attached to "
                                "this email.", os.path.join("tmp", "processed.pdf")))

# #!/usr/bin/env python3
#
# import reports
# import emails
# import os
# from datetime import date
#
# desc_path = os.path.expanduser('~') + '/supplier-data/descriptions/'
# report = []
#
#
# def process_data(data):
#     for item in data:
#         report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
#     return report
#
#
# text_data = []
# for text_file in os.listdir(desc_path):
#     with open(desc_path + text_file, 'r') as f:
#         text_data.append([line.strip() for line in f.readlines()])
#         f.close()
#
# if __name__ == "__main__":
#     """
#     You will need to pass the following arguments to the reports.generate_report method:
#     * the text description processed from the text files as the paragraph argument,
#     * the report title as the title argument,
#     * and the file path of the PDF to be generated as the attachment argument (use ‘/tmp/processed.pdf')
#     """
#     summary = process_data(text_data)
#     paragraph = "<br/><br/>".join(summary)
#     title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
#     attachment = "/tmp/processed.pdf"
#     reports.generate_report(attachment, title, paragraph)
#
#     # Send the email
#     """
#     Use the following details to pass the parameters to emails.generate_email():
#
#     * From: automation@example.com
#     * To: username@example.com
#         * Replace username with the username given in the Connection Details Panel on the right hand side.
#     * Subject line: Upload Completed - Online Fruit Store
#     * E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
#     * Attachment: Attach the path to the file processed.pdf
#     """
#     subject = "Upload Completed - Online Fruit Store"
#     sender = "automation@example.com"
#     receiver = "{}@example.com".format(os.environ.get('USER'))
#     body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
#     message = emails.generate(sender, receiver, subject, body, attachment)
#     emails.send(message)
