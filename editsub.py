from datetime import time, date, datetime, timedelta

def str2datetime(time_str: str) -> time:
    """string to time"""
    time_set = time_str.split(':')
    hour = int(time_set[0])
    minute= int(time_set[1])
    second = int(time_set[2].split(',')[0])
    mili = time_set[2].split(',')[1]
    len_mili = len(mili)
    if 6 - len_mili > 0:
        for i in range(6-len_mili):
            mili+='0'

    date_ = date(1, 1, 1)
    time_ = time(hour,minute,second,int(mili))
    datetime_ = datetime.combine(date_, time_)
    return datetime_

def minusTime(datetime1: datetime,datetime2: datetime) -> timedelta:
    """Get timedelta"""
    if datetime1 > datetime2:
        return datetime1 - datetime2
    else:
        return datetime2 - datetime1

def main():
    hour = input('Hour: ')
    minute = input('Minute: ')
    second = input('Second: ')
    milisecond = input('Milisecond: ')
    position = input('Position sub: ')

    user_input = str2datetime(hour+':'+minute+':'+second+','+milisecond)
    with open('C:/Users/truon/Desktop/filesub.srt', 'r', encoding='utf-8') as f:
        list_subs = f.readlines()
    
    # lay ra list time duoc chuan hoa
    x = 1
    list_times = [] # important!
    for i in range(len(list_subs)):
        if str(x) == list_subs[i][0:-1]:
            x+=1
            list_times.extend(list_subs[i+1][0:-1].split(' --> '))
    
    # loai bo credit sub
    list_times = list_times[int(position)*2-2:len(list_times)]
    new_time = [] # la list_times sau khi dc xu ly ---important!
    first_line = str2datetime(list_times[0])

    # xu ly time theo input cua user
    delta = minusTime(user_input, first_line)
    if user_input > first_line:
        for i in list_times:
            edited = str2datetime(i) + delta
            # final
            str_to_sub = edited.strftime(r"%H:%M:%S,%f")[0:-3]
            new_time.append(str_to_sub)
    elif user_input < first_line:
        for i in list_times:
            edited = str2datetime(i) - delta
            # final
            str_to_sub = edited.strftime(r"%H:%M:%S,%f")[0:-3]
            new_time.append(str_to_sub)

    # xuat ra file moi
    print('Tong so dong sub la: ', x-1)
    j = 0
    z = int(position)
    for i in range(x):
        if str(z) == list_subs[i][0:-1]:
            # print('replace!!!')
            index_sub_order = list_subs.index(list_subs[i])

            text_replace = new_time[j*2] + ' --> '+ new_time[j*2+1] + '\n'
            list_subs[index_sub_order+1] = text_replace
            j+=1
            z+=1
    # print(list_subs)

    # output --> new sub file
    with open('C:/Users/truon/Desktop/new_sub.srt','w', encoding='utf-8') as f:
        f.writelines(list_subs)
    print('Chuc ban xem phim vui ve')


if __name__ == "__main__":
    main()

