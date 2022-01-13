import argparse, subprocess, time
from os.path import expanduser

HOMEPATH = expanduser('~')
ffmpegbar = 'node "'+HOMEPATH+'\\AppData\Roaming\\npm\\node_modules\\ffmpeg-progressbar-cli\\lib\\main.js"'

parser = argparse.ArgumentParser(description='osu2mp4/danser highfps video resampler')
parser = argparse.ArgumentParser(prog='osu-resampler')
parser.add_argument('--gui', nargs='?', default='ffmpeg', type=str, const='ffmpeg', help='Choice of type of gui - ffmpeg/ffbar(ffmpeg-bar) (default=ffmpeg)')
parser.add_argument('-i', help='Full path to video file you want to resample. Without this the program wont run!', nargs=1, type=str)
parser.add_argument('-fps', help='''FPS of the video you're trying to resample.''', nargs=1, type=int)
parser.add_argument('-crf', help='Quality of the video, the lower the better (0 is lossless, default=7).', nargs='?', type=int, default=7)
parser.add_argument('output', metavar='O', type=str, nargs=2, help='<Output folder path> <Output video name> (The space in between is needed).')
args = parser.parse_args()

if ((args.fps[0] != None) and (args.i[0] != None)):
    print("Please do not change anything in the working folder while the program is running!")
    print("The resampling will start in 5 seconds")
    time.sleep(5)
    if (args.gui == 'ffmpeg'):
        shell_command = 'ffmpeg -i "'+args.i[0]+'" -preset ultrafast -c:v libx264 -b:v 12M -movflags faststart -crf '+str(args.crf)+' -vf tmix=frames='+str(args.fps[0]//60)+':weights="1",fps=60 -an "'+args.output[0]+r'\output-an.mp4"'
        subprocess.run(shell_command)
        shell_command = 'ffmpeg -i "'+args.i[0]+'" -vn -c:a aac -b:a 320k "'+args.output[0]+'\output-vn.aac"'
        subprocess.run(shell_command)
        shell_command = 'ffmpeg -i '+args.output[0]+r'\output-an.mp4 -i "'+args.output[0]+'\output-vn.aac" -c:a copy -c:v copy "'+args.output[0]+'\\'+args.output[1]+'".mp4'
        subprocess.run(shell_command)
    elif (args.gui == 'ffbar'):
        shell_command = ffmpegbar+' -i "'+args.i[0]+'" -preset ultrafast -c:v libx264 -b:v 12M -movflags faststart -crf '+str(args.crf)+' -vf tmix=frames='+str(args.fps[0]/60)+':weights="1",fps=60 -an "'+args.output[0]+r'\output-an.mp4"'
        subprocess.run(shell_command)
        shell_command = ffmpegbar+' -i "'+args.i[0]+'" -vn -c:a aac -b:a 320k "'+args.output[0]+r'\output-vn.aac"'
        subprocess.run(shell_command)
        shell_command = ffmpegbar+' -i "'+args.output[0]+r'\output-an.mp4" -i "'+args.output[0]+r'\output-vn.aac" -c:a copy -c:v copy "'+args.output[0]+'\\'+args.output[1]+'.mp4"'
        subprocess.run(shell_command)
subprocess.run('del "'+args.output[0]+r'\output-an.mp4"')
subprocess.run('del "'+args.output[0]+r'\output-vn.aac"')
print('-------------------------------------FIN-------------------------------------')
