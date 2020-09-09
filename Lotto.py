from openpyxl import load_workbook
import random

results = []

def get_Lotto_numbers(episode):
    results = []
    file_name = "./Lotto.xlsx"
    wb = load_workbook(filename=file_name, data_only=True)
    ws = wb.active
    for i in range(1, episode):
        result = []
        #result.append(ws['b'+str(i + 3)].value)
        result.append(ws['n'+str(i + 3)].value)
        result.append(ws['o'+str(i + 3)].value)
        result.append(ws['p'+str(i + 3)].value)
        result.append(ws['q'+str(i + 3)].value)
        result.append(ws['r'+str(i + 3)].value)
        result.append(ws['s'+str(i + 3)].value)
        results.append(result)
    
    #print(results)
    return results

def get_Lotto():
    예상수 = list(range(1, 46))#[10, 12, 13, 16, 17, 18, 20, 21, 22, 30, 33, 34, 35, 36, 37, 43, 45]
    약한수 = list(range(1, 46))
    고정수 = list(range(1, 46))#[10, 12, 13, 16, 17, 18, 20, 21, 22, 30, 33, 34, 35, 36, 37, 43, 45]
    확률 =  [0,1,2,3,4,5,6,7,8,9]
    예 = 0
    약 = 0
    고 = 0

    로또 = []

    for i in range(1, 7):
        if i < 2:
            if random.choice(확률) < 5:
                random.shuffle(고정수)
                num = random.choice(고정수)
                고정수.remove(num)
                예상수.remove(num)
                로또.append(num)
                고 += 1
            else:
                pro = random.choice(확률)            
                if pro < 1:
                    print(pro)
                    random.shuffle(약한수)
                    num = random.choice(약한수)
                    약한수.remove(num)
                    로또.append(num)
                    약 += 1
                else:
                    random.shuffle(예상수)
                    num = random.choice(예상수)
                    예상수.remove(num)
                    로또.append(num)
                    예 += 1  
        else:
            pro = random.choice(확률)            
            if pro < 1:
                print(pro)
                random.shuffle(약한수)
                num = random.choice(약한수)
                약한수.remove(num)
                로또.append(num)
                약 += 1
            else:
                random.shuffle(예상수)
                num = random.choice(예상수)
                예상수.remove(num)
                로또.append(num)  
                예 +=1          
    로또.sort()
    return 로또
    #print(로또)

    #print("고" + str(고) + "예" + str(예) + "약" + str(약))


# old_Lotto_numbers = get_Lotto_numbers(915)
# numbers = [[4,5,15,20,23,41],[4,15,17,18,41,45],[9,10,24,31,40,41],[4,15,25,31,32,43],[5,9,17,25,32,35]]
# for num in numbers:
#     if num in old_Lotto_numbers:
#         print("있다")

# 끝수 파악
def end_num(numbers):
    # 딕셔너리 제작
    end_num_dict = {}
    for i in range(0, 10):
        end_num_dict[i] = 0
    
    for num in numbers:
        if len(str(num)) == 1:
            end_num_dict[num] += 1
        else:
            end_num_dict[int(str(num)[1])] += 1
            # print(str(num)[1])
    
    return end_num_dict
    
    # 끝수 확인 후 딕셔너리에 포함



# 모서리 확률
def edge_num(numbers):
    edge_numbers = [1, 2, 8, 9, 6, 7, 13, 14, 29, 30, 36, 37, 34, 35, 41, 42]
    count = 0
    for num in numbers:
        if num*1.in(edge_numbers):
            count += 1
    return count
    

# 이웃수 확률
def around_num(numbers):
    around_list = []
    for num in numbers:                
        if not num-1.in(around_list):            
            around_list.append(num-1)
        if not num+1.in(around_list):
            around_list.append(num+1)
    return around_list


# round = 924
# lotto_list = get_Lotto_numbers(round)
# # print(lotto_list[-1:5:-1])
# for list in lotto_list[0:10]:
#     print(round, "회차 끝수 정보 : ", end_num(list))
#     print(round, "회차 모서리 개수 : ", edge_num(list))
#     round -= 1


def Lotto():
    old_Lotto_numbers = get_Lotto_numbers(926)
    nums_Lotto = []
    while len(nums_Lotto) < 5:
        num_Lotto = get_Lotto()
        if num_Lotto not in old_Lotto_numbers:
            if edge_num(num_Lotto) != 0 and edge_num(num_Lotto) < 3:
                nums_Lotto.append(num_Lotto)

    print(nums_Lotto)
    
Lotto()
