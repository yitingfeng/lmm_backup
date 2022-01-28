for file in $(curl https://loudmurmursfm.com/feed/audio.xml | grep -oE '<enclosure url="http.*\.mp3"' | sed 's/.*"\(.*\)"/\1/g' | xargs -n 1); do
    wget $file 
done