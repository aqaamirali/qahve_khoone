from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Study Schedule for Midterms', 0, 1, 'C')

    def chapter_title(self, chapter_title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, chapter_title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

content = [
    ("Weeks 1 to 4: Strong Start", """Saturday to Thursday:
- Electric Circuits 1: 2 hours of study + problem solving (3 days a week)
- Differential Equations: 2 hours of study + problem solving (2 days a week)
- Physics 2: 2 hours of study + review (2 days a week)
- Numerical Methods: 1.5 hours of study + practical exercises (2 days a week)
- Family Studies: 1 hour of study (1 day a week)
- Physics Lab 1: 1 hour of review and report preparation (1 day a week)
- Industrial Drawing: 1 hour of study + drawing exercises (1 day a week)

Friday:
- Overall review of subjects and key points
- Practice tests and mock exams"""),

    ("Weeks 5 to 8: Strengthening and Review", """Saturday to Thursday:
- Electric Circuits 1: 1.5 hours of review + solving complex problems (3 days a week)
- Differential Equations: 1.5 hours of review + exercises (2 days a week)
- Physics 2: 1.5 hours of review + problem-solving (2 days a week)
- Numerical Methods: 1.5 hours of review + programming (2 days a week)
- Family Studies: 1 hour of study (1 day a week)
- Physics Lab 1: 1 hour of review and completing reports (1 day a week)
- Industrial Drawing: 1 hour of drawing practice (1 day a week)

Friday:
- Overall review of subjects and solving mock test papers
- Reviewing notes and key points for each subject"""),

    ("Weeks 9 to 12: Final Preparation for Midterms", """Saturday to Thursday:
- Electric Circuits 1: 1 hour of final review + problem-solving (3 days a week)
- Differential Equations: 1 hour of final review + solved problems (2 days a week)
- Physics 2: 1 hour of final review + exercises (2 days a week)
- Numerical Methods: 1 hour of final review + programming exercises (2 days a week)
- Family Studies: 1 hour of review (1 day a week)
- Physics Lab 1: 1 hour of review and completing reports (1 day a week)
- Industrial Drawing: 1 hour of final review (1 day a week)

Friday:
- Overall review of subjects
- Taking mock exams
- Reviewing notes and study materials"""),

    ("Additional Tips", """1. Rest time: 10 minutes break after every 1 hour of study.
2. Mental and physical preparation: light exercises and healthy nutrition.
3. Use of supplementary resources: educational videos, additional notes, and study groups.
4. Stress management: breathing techniques and meditation.""")
]

# build PDF
pdf = PDF()
pdf.add_page()

for title, body in content:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output('Study_Schedule.pdf')

print("Study_Schedule.pdf has been created successfully!")
