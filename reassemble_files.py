import shutil

# Define the parts
parts = [
    'colorization_release_v2.caffemodel.gz.part1',
    'colorization_release_v2.caffemodel.gz.part2',
    'colorization_release_v2.caffemodel.gz.part3',
    'colorization_release_v2.caffemodel.gz.part4',
    'colorization_release_v2.caffemodel.gz.part5',
]

# Combine the parts into the original compressed file
with open('colorization_release_v2.caffemodel.gz', 'wb') as f_out:
    for part in parts:
        with open(part, 'rb') as f_in:
            shutil.copyfileobj(f_in, f_out)
