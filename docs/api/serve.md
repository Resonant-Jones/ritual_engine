# NPC Sys environment 

::: npcpy.serve
    options:
      show_source: true
      members: true
      filters:
        - "!^_"          # Hide private members
        - "!^[A-Z]{2,}"  # Hide constants (all-caps)
        - "!test_"       # Hide test functions
      inherited_members: false
      show_root_heading: false
      show_if_no_docstring: true