# ------------------
# Messages
joomla_check = "\n[cyan][INF] Trying to detect Joomla... [/]"
version_check = "\n[cyan][INF] Trying to get Joomla version... [/]"

success_first = "[green][INF] Detected Joomla on 1° check. [/]"
fail_first = "[yellow][WRN] Can't detect Joomla admin login, passing check... (1° check)"

success_second = "[green][INF] Detected Joomla on 2° check. [/]"
fail_second = "[yellow][WRN] Can't detect Joomla logo, passing check... (2° check) [/]"

success_third = "[green][INF] Detected Joomla on 3° check. [/]"
fail_third = "[yellow][WRN] Can't detect Joomla on body, passing check... (3° check) [/]"

success_fourth = "[green][INF] Detected Joomla on 4° check. [/]"
fail_fourth = "[yellow][WRN] Can't detect Joomla meta generator tag, passing check... (4° check) [/]"

success_fifth = "[green][INF] Detected Joomla on 5° check. [/]"
fail_fifth = "[yellow][WRN] Can't detect Joomla search method, passing check... (5° check) [/]"

fail_version_first = "[red][ERR] Can't detect Joomla version on 1° check... [/]"
fail_version_second = "[red][ERR] Can't detect Joomla version on 2° check, stopping... [/]"

last_chance = "[green][INF] 50% chance that Joomla has been detected... [/]"

invalid_url = "[red][ERR] Invalid URL, please use http or https before the URL. [/]"
config_files_scan = "[cyan][INF] Trying to find config files... [/]"
not_detected = "[red][ERR] Joomla was not detected, stopping... [/]"
false_positive = "[red][ERR] Possible false positve on Joomla detection. [/]"
xml_parse = "[red][ERR] Can't parse Joomla XML, stopping... \n [/]"


# ------------------
# Paths
joomla_admin_path = "/administrator"
joomla_admin_logo_path = "/administrator/templates/khepri/images/h_green/j_header_left.png"
robots_file = "/robots.txt"
manifest_joomla = "/administrator/manifests/files/joomla.xml"
language_joomla = "/language/en-GB/en-GB.xml"