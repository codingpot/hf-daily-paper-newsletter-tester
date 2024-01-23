import os
import yaml
import requests
import argparse

import magic
from moviepy.editor import VideoFileClip

def is_video(filename):
  file_type = magic.from_file(filename, mime=True)
  return file_type.startswith('video/')

def main(args):
  for filename in os.listdir(args.yaml_dir):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
      file_path = os.path.join(args.yaml_dir, filename)

      with open(file_path, 'r') as file:
        parsed_yaml = yaml.safe_load(file)

      thumbnail_url = parsed_yaml['thumbnail']
      if is_video(thumbnail_url):
        print(f"video type found: {thumbnail_url}")
        tmp_filename = os.path.normpath(url).split(os.sep)[-1]
        arxiv_id = os.path.normpath(parsed_yaml['link']).split(os.sep)[-1]
        gif_filename = f"{args.gif_output_path}/{arxiv_id}.gif"

        response = requests.get(thumbnail_url)
        response.raise_for_status()

        with open(tmp_filename, 'wb') as f:
          f.write(response.content)
        print(f"File downloaded and saved as {tmp_filename}")
        
        print(f"converting {tmp_filename} => {gif_filename}")
        videoClip = VideoFileClip(tmp_filename)
        videoClip.speedx(args.speedx).to_gif(gif_filename)

        print(f"remove {tmp_filename}")
        os.remove(tmp_filename)

        parsed_yaml['thumbnail'] = f"https://github.com/{args.gif_output_github_repo}/blog/main/{gif_filename}"
        with open(file_path, 'w') as file:
            yaml.dump(parsed_yaml, file, default_flow_style=False)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--yaml-dir', type=str, default="current")
  parser.add_argument('--gif-output-github-repo', type=str, default="codingpot/hf-daily-paper-newsletter-tester")
  parser.add_argument('--gif-output-dir', type=str, default="assets")
  parser.add_argument('--speedx', type=int, default=5)

  args = parser.parse_args()
  main(args)
