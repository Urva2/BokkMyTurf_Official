import os
import glob

override_css = """
  <!-- AUTO-INJECTED THEME OVERRIDE -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
  <style>
    /* VARIABLES REDEFINITION */
    :root {
      --bg-color: #F5F5DC !important;
      --text-color: #556B2F !important;
      --accent: #6B8E23 !important;
      --accent-primary: #6B8E23 !important;
      --bg-secondary: #EBEBD3 !important;
      --bg-tertiary: #DFDFC1 !important;
      --text-muted: #6B8E23 !important;
      --primary: #556B2F !important;
      --primary-hover: #6B8E23 !important;
      --text-main: #556B2F !important;
      --bg-card: rgba(85, 107, 47, 0.05) !important;
      --bg-footer: #556B2F !important;
    }

    /* TYPOGRAPHY & BODY */
    body, p, h1, h2, h3, h4, h5, h6, a, span, div, td, th, label, input, select, textarea, button {
      font-family: 'Lora', serif !important;
    }
    body {
      background-color: #F5F5DC !important;
      color: #556B2F !important;
    }
    
    /* INVERTED HEADERS, FOOTERS & SIDEBARS */
    header, footer, .sidebar, .page-header, .top-header, .nav-left, .nav-right, .nav-center, .navbar {
      background-color: #556B2F !important;
      color: #F5F5DC !important;
      border-color: #6B8E23 !important;
    }
    header a, footer a, .sidebar a, .page-header h1, .sidebar-name, .sidebar-email, .top-header-left h1, .navbar a, .navbar i, .navbar span {
      color: #F5F5DC !important;
    }
    
    /* CARDS & CONTAINERS */
    .summary-card, .tab-content, .booking-item, .turf-card, .pending-section, .auth-card, .glass-card, .dashboard-card, .admin-card {
      background-color: #EBEBD3 !important;
      border: 1px solid #DFDFC1 !important;
      box-shadow: 0 4px 15px rgba(85, 107, 47, 0.1) !important;
    }
    .summary-card-value, .card-value, .turf-name-cell, .auth-card h2, h1, h2, h3, .booking-player, .turf-info h3 {
      color: #556B2F !important;
    }
    
    /* INPUTS & FORMS */
    input, select, textarea {
      background-color: #F5F5DC !important;
      color: #556B2F !important;
      border: 1px solid #6B8E23 !important;
    }
    input:focus, select:focus, textarea:focus {
      border-color: #556B2F !important;
      outline: none !important;
    }
    
    /* BUTTONS */
    .btn, .btn-primary, .btn-add-turf, .btn-login, .btn-signup, .primary-cta, .submit-btn, .view-details-btn, .action-btn {
      background-color: #556B2F !important;
      color: #F5F5DC !important;
      border: none !important;
    }
    .btn:hover, .btn-primary:hover, .btn-add-turf:hover, .primary-cta:hover, .submit-btn:hover, .view-details-btn:hover, .action-btn:hover {
      background-color: #6B8E23 !important;
      color: #F5F5DC !important;
    }
    
    /* TABLES */
    table thead th {
      color: #556B2F !important;
      border-bottom-color: #6B8E23 !important;
    }
    table tbody td, .pending-table tbody tr {
      border-bottom-color: #DFDFC1 !important;
      color: #556B2F !important;
    }
    .pending-table tbody tr:hover {
       background-color: #DFDFC1 !important;
    }
    
    /* MISC RESETS */
    .text-muted, .date-cell, .owner-name-cell, .city-cell, .booking-contact {
       color: #6B8E23 !important;
    }
    .tab-btn {
       color: #6B8E23 !important;
    }
    .tab-btn.active {
       color: #556B2F !important;
       border-bottom-color: #556B2F !important;
    }
    .sidebar-btn {
       background-color: #DFDFC1 !important;
       color: #556B2F !important;
       border-color: #6B8E23 !important;
    }
  </style>
</head>"""

template_dir = r"c:\Users\PRIYANSH PATEL\BokkMyTurf_Official\turf_connect\templates"
skip_files = ["home.html", "player_home.html", "owner_home.html"]

for filepath in glob.glob(os.path.join(template_dir, "*.html")):
    filename = os.path.basename(filepath)
    if filename in skip_files:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if we already injected to avoid duplicating
    if "AUTO-INJECTED THEME OVERRIDE" in content:
        continue
        
    # Inject right before </head>
    new_content = content.replace('</head>', override_css)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Successfully injected CSS override block into all target templates.")
