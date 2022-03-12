import pandas
from faker import Faker

fake = Faker()

# read csv file
df = pandas.read_csv('data.csv')

# # get each row
# for index, row in df.iterrows():
#     caption = row['caption']
#     img_name = row['image']
#     is_done = row['done']
#     if str(is_done).lower().strip() == 'nan':
#         is_done = False
#     else:
#         is_done = True

    
# add new row to csv file
for i in range(1000):
    caption = fake.word()
    img_name = 'sample.png'
    is_done = ''
    df.loc[len(df)] = [caption, img_name, is_done]
    df.to_csv('data.csv', index=False)
