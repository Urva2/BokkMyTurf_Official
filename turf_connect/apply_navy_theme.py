import os
import glob
import re

new_override_css = """
  <!-- AUTO-INJECTED THEME OVERRIDE -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
  <style>
    /* VARIABLES REDEFINITION */
    :root {
      --bg-color: #F5F5DC !important;
      --text-primary: #0A2540 !important;
      --text-secondary: #3A4F7A !important;
      --accent: #2E8B57 !important;
      --border-color: #D6D6B8 !important;
      
      /* Legacy aliases for compatibility */
      --text-color: #0A2540 !important;
      --accent-primary: #2E8B57 !important;
      --bg-secondary: #EBEBD3 !important;
      --bg-tertiary: #DFDFC1 !important;
      --text-muted: #3A4F7A !important;
      --primary: #0A2540 !important;
      --primary-hover: #3A4F7A !important;
      --text-main: #0A2540 !important;
      --bg-card: rgba(10, 37, 64, 0.05) !important;
      --bg-footer: #0A2540 !important;
    }

    /* TYPOGRAPHY & BODY */
    body, p, h1, h2, h3, h4, h5, h6, a, span, div, td, th, label, input, select, textarea, button {
      font-family: 'Lora', serif !important;
    }
    body {
      background-color: #F5F5DC !important;
      color: #0A2540 !important;
    }
    
    /* INVERTED HEADERS, FOOTERS & SIDEBARS */
    header, footer, .sidebar, .page-header, .top-header, .nav-left, .nav-right, .nav-center, .navbar {
      background-color: #0A2540 !important;
      color: #F5F5DC !important;
      border-color: #D6D6B8 !important;
    }
    header a, footer a, .sidebar a, .page-header h1, .sidebar-name, .sidebar-email, .top-header-left h1, .navbar a, .navbar i, .navbar span {
      color: #F5F5DC !important;
    }
    
    /* CARDS & CONTAINERS */
    .summary-card, .tab-content, .booking-item, .turf-card, .pending-section, .auth-card, .glass-card, .dashboard-card, .admin-card {
      background-color: #F5F5DC !important;
      border: 1px solid #D6D6B8 !important;
      box-shadow: 0 4px 15px rgba(10, 37, 64, 0.08) !important;
    }
    .summary-card-value, .card-value, .turf-name-cell, .auth-card h2, h1, h2, h3, .booking-player, .turf-info h3 {
      color: #0A2540 !important;
    }
    
    /* INPUTS & FORMS */
    input, select, textarea {
      background-color: #F5F5DC !important;
      color: #0A2540 !important;
      border: 1px solid #D6D6B8 !important;
    }
    input:focus, select:focus, textarea:focus {
      border-color: #2E8B57 !important;
      outline: none !important;
    }
    
    /* BUTTONS */
    .btn, .btn-primary, .btn-add-turf, .btn-login, .btn-signup, .primary-cta, .submit-btn, .view-details-btn, .action-btn {
      background-color: #2E8B57 !important;
      color: #F5F5DC !important;
      border: none !important;
    }
    .btn:hover, .btn-primary:hover, .btn-add-turf:hover, .primary-cta:hover, .submit-btn:hover, .view-details-btn:hover, .action-btn:hover {
      background-color: #246d44 !important;
      color: #F5F5DC !important;
    }
    
    /* TABLES */
    table thead th {
      color: #0A2540 !important;
      border-bottom-color: #D6D6B8 !important;
    }
    table tbody td, .pending-table tbody tr {
      border-bottom-color: #D6D6B8 !important;
      color: #0A2540 !important;
    }
    .pending-table tbody tr:hover {
       background-color: rgba(10, 37, 64, 0.05) !important;
    }
    
    /* MISC RESETS */
    .text-muted, .date-cell, .owner-name-cell, .city-cell, .booking-contact {
       color: #3A4F7A !important;
    }
    .tab-btn {
       color: #3A4F7A !important;
    }
    .tab-btn.active {
       color: #2E8B57 !important;
       border-bottom-color: #2E8B57 !important;
    }
    .sidebar-btn {
       background-color: rgba(10, 37, 64, 0.05) !important;
       color: #0A2540 !important;
       border-color: #D6D6B8 !important;
    }
  </style>
</head>"""

template_dir = r"c:\Users\PRIYANSH PATEL\BokkMyTurf_Official\turf_connect\templates"

# Files that we need to manually regex replace because they don't have the auto-injected block or we want to fix their native CSS
native_css_files = ["player_home.html", "owner_home.html", "browse.html", "playerdashboard.html", "ownerdashboard.html"]

for filepath in glob.glob(os.path.join(template_dir, "*.html")):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False

    # 1. Update Auto-injected theme override blocks
    # Using regex to find the block starting with <!-- AUTO-INJECTED THEME OVERRIDE --> up to </head>
    pattern = r"<!-- AUTO-INJECTED THEME OVERRIDE -->.*?</head>"
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_override_css.strip(), content, flags=re.DOTALL)
        modified = True

    # 2. String replacements for native files
    if filename in native_css_files:
        # replace variables definition
        content = content.replace("--text-color: #556B2F;", "--text-primary: #0A2540;\n            --text-secondary: #3A4F7A;\n            --border-color: #D6D6B8;")
        content = content.replace("--accent: #6B8E23;", "--accent: #2E8B57;")
        
        # replace usage
        content = content.replace("var(--text-color)", "var(--text-primary)")
        content = content.replace("border-bottom: 2px solid var(--accent);", "border-bottom: 2px solid var(--border-color);")
        
        # replace specific hovers
        content = content.replace("background-color: var(--bg-color);\n            color: var(--text-color) !important;", "background-color: var(--accent);\n            color: var(--bg-color) !important;")
        content = content.replace("background-color: #e3e3cb;", "background-color: #246d44;")
        
        # Button explicit styles (from mass_style.py matching)
        content = content.replace("background-color: #556B2F;", "background-color: var(--text-primary);")
        content = content.replace("color: #556B2F;", "color: var(--text-primary);")
        
        # footer specific fixes
        content = content.replace("background-color: #556B2F;", "background-color: var(--text-primary);")
        
        # Primary CTAs
        content = content.replace("background-color: var(--text-color);\n            color: var(--bg-color);", "background-color: var(--accent);\n            color: var(--bg-color);")
        
        # Replace remaining explicit colors
        content = content.replace("#556B2F", "var(--text-primary)")
        content = content.replace("#6B8E23", "var(--accent)")
        
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

print("Successfully injected new Navy Blue CSS override block into all target templates.")
