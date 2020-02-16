from PIL import Image
import os

def combine2Pdf( folderPath, pdfFilePath ):
    files = os.listdir( folderPath )
    pngFiles = []
    sources = []
    for file in files:
        if 'png' in file:
            pngFiles.append( folderPath + file )
    pngFiles.sort()
    output = Image.open( pngFiles[0] )
    pngFiles.pop( 0 )
    for file in pngFiles:
        pngFile = Image.open( file )
        if pngFile.mode == "RGB":
            pngFile = pngFile.convert( "RGB" )
        sources.append( pngFile )
    output.save( pdfFilePath, "pdf", save_all=True, append_images=sources )

if __name__ == "__main__":
    folder = "/Users/weiyang/Desktop/pngFiles/"
    pdfFile = "/Users/weiyang/Desktop/contract.pdf"
    combine2Pdf( folder, pdfFile )
