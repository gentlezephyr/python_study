import PySimpleGUI as sg
import extractor_zip


def firstRow(textone, inputone, chooseone):
    return sg.Text(textone), sg.Input(inputone), sg.FileBrowse(chooseone, key='choose1')


def secondRow(texttwo, inputtwo, choosetwo):
    return sg.Text(texttwo), sg.Input(inputtwo), sg.FolderBrowse(choosetwo, key='choose2')


layout = [
    *[firstRow('Select archive:', '', 'Choose')],
    *[secondRow('Select path:', '', 'Choose')],
    [sg.Button('Extract')], [sg.Text(key='output', text_color='green')]
]

window = sg.Window('Extractor', layout)

while True:
    event, values = window.read()
    print(event, values)
    file_to_extract = values['choose1']
    folder_to_save = values['choose2']
    extractor_zip.extract_zip(file_to_extract, folder_to_save)
    window['output'].update(value='Done')
window.close()
