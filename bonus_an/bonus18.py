import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('Black')

label1 = sg.Text("Select Archive")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key = "archive")

label2 = sg.Text("Select Destination")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key = "folder")


extract_button = sg.Button("Extract")
output_label = sg.Text(key = "output", text_color= "green")


window = sg.Window("Archive Extractor",
                   layout = [[label1, input1, button1],
                             [label2, input2, button2],
                             [extract_button, output_label]])

while True:
    event,values = window.read()
    print(event,values)
    archivepath=values["archive"]
    destination_path=values["folder"]
    extract_archive(archivepath, destination_path)
    window["output"].update(value="Extraction Completed")
#window.read()
window.close()