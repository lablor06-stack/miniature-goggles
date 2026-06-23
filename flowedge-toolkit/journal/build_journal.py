"""Generates the FlowEdge Trading Journal (.xlsx) with auto-calculating stats.
Run: python3 build_journal.py
Output: FlowEdge_Trading_Journal.xlsx
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ACCENT = "1F2937"   # dark slate
HEAD   = "111827"
GREEN  = "DCFCE7"
RED    = "FEE2E2"
LIGHT  = "F3F4F6"

thin = Side(style="thin", color="D1D5DB")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()

# ----------------------------------------------------------------- Trades sheet
ws = wb.active
ws.title = "Trades"

headers = ["Date", "Pair/Asset", "Direction", "Session", "Setup",
           "Entry", "Stop", "Target", "Lots/Size", "Risk %",
           "Result (R)", "P/L", "Outcome", "Notes"]

for c, h in enumerate(headers, start=1):
    cell = ws.cell(row=1, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=HEAD)
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = border

widths = [12, 12, 10, 14, 16, 10, 10, 10, 10, 8, 11, 12, 12, 30]
for i, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w

# Data validation dropdowns
dv_dir = DataValidation(type="list", formula1='"Long,Short"', allow_blank=True)
dv_out = DataValidation(type="list", formula1='"Win,Loss,Break-even"', allow_blank=True)
dv_ses = DataValidation(type="list", formula1='"London,New York,Asia,Other"', allow_blank=True)
dv_set = DataValidation(type="list", formula1='"FVG,BOS,CHoCH,Liquidity Sweep,Kill Zone"', allow_blank=True)
for dv in (dv_dir, dv_out, dv_ses, dv_set):
    ws.add_data_validation(dv)
dv_dir.add("C2:C1000")
dv_ses.add("D2:D1000")
dv_set.add("E2:E1000")
dv_out.add("M2:M1000")

# Pre-format 1000 empty rows
for r in range(2, 1001):
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=r, column=c)
        cell.border = border
        if c == 13:  # Outcome conditional-ish via fill formula not possible; leave plain
            pass
ws.freeze_panes = "A2"

# ---------------------------------------------------------------- Dashboard
dash = wb.create_sheet("Dashboard")
dash.sheet_view.showGridLines = False
dash.column_dimensions["A"].width = 28
dash.column_dimensions["B"].width = 18

title = dash.cell(row=1, column=1, value="FlowEdge — Performance Dashboard")
title.font = Font(bold=True, size=16, color="FFFFFF")
title.fill = PatternFill("solid", fgColor=ACCENT)
dash.merge_cells("A1:B1")
dash.cell(row=1, column=2).fill = PatternFill("solid", fgColor=ACCENT)

stats = [
    ("Total trades",        '=COUNTA(Trades!A2:A1000)'),
    ("Wins",                '=COUNTIF(Trades!M2:M1000,"Win")'),
    ("Losses",              '=COUNTIF(Trades!M2:M1000,"Loss")'),
    ("Break-even",          '=COUNTIF(Trades!M2:M1000,"Break-even")'),
    ("Win rate",            '=IFERROR(B3/(B3+B4),0)'),
    ("Total R",             '=SUM(Trades!K2:K1000)'),
    ("Average R",           '=IFERROR(AVERAGE(Trades!K2:K1000),0)'),
    ("Net P/L",             '=SUM(Trades!L2:L1000)'),
    ("Best trade (P/L)",    '=IFERROR(MAX(Trades!L2:L1000),0)'),
    ("Worst trade (P/L)",   '=IFERROR(MIN(Trades!L2:L1000),0)'),
    ("Expectancy (R/trade)",'=IFERROR(AVERAGE(Trades!K2:K1000),0)'),
]
for i, (label, formula) in enumerate(stats, start=2):
    lc = dash.cell(row=i + 1, column=1, value=label)
    lc.font = Font(bold=True, color="111827")
    lc.fill = PatternFill("solid", fgColor=LIGHT)
    lc.border = border
    vc = dash.cell(row=i + 1, column=2, value=formula)
    vc.border = border
    vc.alignment = Alignment(horizontal="center")
    if label == "Win rate":
        vc.number_format = "0.0%"

# Setup breakdown
dash.cell(row=15, column=1, value="Performance by Setup").font = Font(bold=True, size=12)
dash.cell(row=16, column=1, value="Setup").font = Font(bold=True)
dash.cell(row=16, column=2, value="Total R").font = Font(bold=True)
setups = ["FVG", "BOS", "CHoCH", "Liquidity Sweep", "Kill Zone"]
for i, s in enumerate(setups, start=17):
    dash.cell(row=i, column=1, value=s).border = border
    f = dash.cell(row=i, column=2,
                  value=f'=SUMIF(Trades!E2:E1000,A{i},Trades!K2:K1000)')
    f.border = border
    f.alignment = Alignment(horizontal="center")

# ----------------------------------------------------------------- Save
wb.save("FlowEdge_Trading_Journal.xlsx")
print("Saved FlowEdge_Trading_Journal.xlsx")
