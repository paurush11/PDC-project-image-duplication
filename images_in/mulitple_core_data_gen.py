import cv2
import numpy as np
import glob
import time
import multiprocessing
import threading


"""
Multiprocessing
"""


image_name = 'c2.jpeg' # origional image path goes here
original = cv2.imread(image_name) 

global image_count
global start_time

image_count = 0
start_time = time.time()

def find_duplicates(image_):
        global image_count
        global start_time
        try:
            image_to_compare = cv2.imread(image_)
            if original.shape == image_to_compare.shape:

                difference = cv2.subtract(original, image_to_compare)
                b, g, r = cv2.split(difference)

                if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                    


                    sift = cv2.xfeatures2d.SIFT_create()
                    kp_1, desc_1 = sift.detectAndCompute(original, None)
                    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

                    index_params = dict(algorithm=0, trees=5)
                    search_params = dict()
                    flann = cv2.FlannBasedMatcher(index_params, search_params)

                    matches = flann.knnMatch(desc_1, desc_2, k=2)

                    good_points = []
                    for m, n in matches:
                        if m.distance < 0.6*n.distance:
                            good_points.append(m)

                    # Define how similar they are
                    number_keypoints = 0
                    if len(kp_1) <= len(kp_2):
                        number_keypoints = len(kp_1)
                    else:
                        number_keypoints = len(kp_2)
            image_count += 1
            return [image_count,round(time.time() - start_time, 5)]

        except Exception as e:
            pass



if __name__ == '__main__':
    

    def filebrowser(ext='', directory=''):
        """
        returns files with an extension
        """
        return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

    image_dir = filebrowser(ext='.jpeg', directory='') # directory='' ==> search images from current to inner sub-directories
    image_dir += filebrowser(ext='.jpg', directory='')
    print(image_dir)
    

    # # 1) Check if 2 images are equals | parallel on cores
    start_time = time.time()
    pool = multiprocessing.Pool() # Equal to number of cores | octa for this pc

    

    inputs = image_dir
    outputs_async = pool.map_async(find_duplicates, inputs)
    print(outputs_async.get())

    print("--- %s seconds ---" % (time.time() - start_time))
    print('Program Executed Completely')



    # [[1, 0.10107], [2, 0.19383], [3, 0.31848], [4, 0.47482], [5, 0.65649], [6, 0.76382], [7, 0.95013], [8, 0.95368], [9, 0.98859], [10, 0.99061], [11, 1.01883], [12, 1.04098], [13, 1.08378], [14, 1.11404], [15, 1.13865], [16, 1.16884], [17, 1.19401], [18, 1.22423], [19, 1.2847], [20, 1.31508], [21, 1.35555], [22, 1.38882], [23, 1.41898], [24, 1.52874], [25, 1.65397], [26, 1.78073], [27, 1.78374], [28, 1.81908], [29, 1.8211], [30, 1.83925], [31, 1.86391], [32, 1.89183], [33, 1.91856], [34, 1.944], [35, 1.97791], [36, 2.01082], [37, 2.03974], [38, 2.06966], [39, 2.09859], [40, 2.12602], [41, 2.15295], 
    # [1, 0.04046], [2, 0.12827], [3, 0.13131], [4, 0.15142], [5, 0.15346], [6, 0.17156], [7, 0.19829], [8, 0.22833], [9, 0.26449], [10, 0.29481], [11, 0.32865], [12, 0.35843], [13, 0.38591], [14, 0.41872], [15, 0.44852], [16, 0.48483], [17, 0.50852], [18, 0.53881], [19, 0.62819], [20, 0.63379], [21, 0.64878], [22, 0.65386], [23, 0.77391], [24, 0.94368], [25, 1.10332], [26, 1.2443], [27, 1.37826], [28, 1.55343], [29, 1.66922], [30, 1.66922], [31, 1.69953], [32, 1.70357], [33, 1.72041], [34, 1.74334], [35, 1.7685], [36, 1.79331], [37, 1.81347], [38, 1.84929], [39, 1.87727], [40, 1.90371], [41, 1.93861], 
    # [1, 0.03834], [2, 0.07619], [3, 0.10097], [4, 0.12913], [5, 0.22199], [6, 0.3615], [7, 0.47616], [8, 0.47616], [9, 0.51298], [10, 0.51298], [11, 0.53324], [12, 0.57362], [13, 0.59583], [14, 0.62143], [15, 0.64674], [16, 0.67694], [17, 0.71121], [18, 0.7456], [19, 0.78612], [20, 0.82114], [21, 0.86908], [22, 0.91129], [23, 0.94103], [24, 1.0463], [25, 1.0463], [26, 1.06897], [27, 1.07099], [28, 1.08909], [29, 1.11122], [30, 1.13635], [31, 1.16153], [32, 1.18619], [33, 1.21193], [34, 1.2412], [35, 1.26597], [36, 1.29636], [37, 1.32613], [38, 1.35596], [39, 1.386], [40, 1.4145], [41, 1.51553], 
    # [1, 0.0151], [2, 0.03026], [3, 0.03026], [4, 0.05499], [5, 0.0777], [6, 0.10495], [7, 0.13014], [8, 0.16488], [9, 0.19061], [10, 0.22497], [11, 0.26132], [12, 0.29167], [13, 0.32205], [14, 0.35533], [15, 0.39088], [16, 0.43024], [17, 0.45041], [18, 0.47513], [19, 0.50187], [20, 0.5251], [21, 0.56043], [22, 0.58469], [23, 0.61536], [24, 0.65024], [25, 0.69608], [26, 0.73044], [27, 0.80043], [28, 0.83022], [29, 0.87617], [30, 0.95011], [31, 1.06997], [32, 1.1283], [33, 1.21491], [34, 1.28172], [35, 1.3504], [36, 1.46198], [37, 1.53466], [38, 1.64032], [39, 1.78561], [40, 1.84028], [41, 1.92926], 
    # [1, 0.04946], [2, 0.06762], [3, 0.16037], [4, 0.28508], [5, 0.41111], [6, 0.50187], [7, 0.91027], [8, 0.94707], [9, 0.99995], [10, 1.05033], [11, 1.09009], [12, 1.1283], [13, 1.16501], [14, 1.20083], [15, 1.23106], [16, 1.26949], [17, 1.30191], [18, 1.35494], [19, 1.39109], [20, 1.84746], [21, 1.88438], [22, 2.08934], [23, 2.16214], [24, 2.18907], [25, 2.215], [26, 2.2519], [27, 2.28732], [28, 2.4913], [29, 2.53317], [30, 2.56908], [31, 2.59601], [32, 2.60398], [33, 2.68676], [34, 2.69525], [35, 2.72767], [36, 2.82242], [37, 2.91486], [38, 2.93515], [39, 2.95047], [40, 2.9807], [41, 3.01493], 
    # [1, 0.04999], [2, 0.08025], [3, 0.11801], [4, 0.15028], [5, 0.17496], [6, 0.221], [7, 0.25124], [8, 0.90017], [9, 0.92991], [10, 0.95009], [11, 0.9994], [12, 1.02005], [13, 1.0503], [14, 1.1001], [15, 1.13832], [16, 1.16049], [17, 1.18517], [18, 1.21089], [19, 1.24128], [20, 1.27163], [21, 1.29984], [22, 1.34031], [23, 1.36531], [24, 1.39511], [25, 1.415], [26, 1.44377], [27, 1.46197], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
    # [1, 0.05244], [2, 0.33336], [3, 0.41253], [4, 0.45291], [5, 0.50497], [6, 0.58817], [7, 0.65675], [8, 0.7195], [9, 0.80043], [10, 0.95745], [11, 1.04257], [12, 1.11304], [13, 1.17369], [14, 1.29521], [15, 1.35241], [16, 1.39739], [17, 1.42669], [18, 1.44688], [19, 1.48723], [20, 1.52252], [21, 1.5581], [22, 1.58633], [23, 1.63929], [24, 1.6897], [25, 1.69278], [26, 1.73258], [27, 1.77265], 
    # [1, 0.0505], [2, 0.06759], [3, 0.10286], [4, 0.20385], [5, 0.2579], [6, 0.753], [7, 1.2979], [8, 1.61863], [9, 1.69274], [10, 1.7827], [11, 1.86088], [12, 2.00849], [13, 2.08978], [14, 2.14763], [15, 2.24986], [16, 2.32267], [17, 2.45383], [18, 2.55755], [19, 2.61839], [20, 2.69121], [21, 2.72014], [22, 2.74607], [23, 2.82386], [24, 2.93274], [25, 3.0442], [26, 3.13758], [27, 3.4926], [28, 3.5229], [29, 3.55268], [30, 3.58796], [31, 3.6383], [32, 3.68272], [33, 3.72259], [34, 3.75753], [35, 3.79281], [36, 3.84024], [37, 3.89509], [38, 3.9261], [39, 3.96121], [40, 4.38345], [41, 4.42143], 
    # [28, 1.60549], [29, 1.64588], [30, 1.66611], [31, 1.6911], [32, 1.72001], [33, 1.75031], [34, 1.90919], [35, 1.9421], [36, 1.97102], [37, 1.99895], [38, 2.00693], [39, 2.08722], [40, 2.09919], [41, 2.13111], 
    # [42, 2.19892], [43, 2.26575], [44, 2.28321], [45, 2.29717], [46, 2.3231], [47, 2.34205], [48, 2.36699], [49, 2.38893], [50, 2.40688], [51, 2.4378], [52, 2.46273], [53, 2.50413], [54, 2.53106], [55, 3.07496], [56, 3.13511], [57, 3.16031], [58, 3.20273], [59, 3.22487], [60, 3.26114], [61, 3.29143], [62, 3.31529], [63, 3.34507], [64, 3.37024], [65, 3.3945], [66, 3.43531], [67, 3.46362], [68, 3.50004], 
    # [42, 1.54581], [43, 1.566], [44, 1.59428], [45, 1.61661], [46, 1.63481], [47, 1.64693], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [48, 1.68127], [49, 1.98115], [50, 2.07242], [51, 2.13325], [52, 2.18113], [53, 2.25991], [54, 2.31727], 
    # [28, 1.82972], [29, 1.89654], [30, 2.04765], [31, 2.10449], [32, 2.16433], [33, 2.21121], [34, 2.32242], [35, 2.38027], [36, 2.43463], [37, 2.46256], [38, 2.47853], [39, 2.5234], [40, 2.55431], [41, 2.59221], [42, 2.61914], [43, 2.68], [44, 2.74382], [45, 2.74981], [46, 2.79968], [47, 2.84019], [48, 2.84223], [49, 2.86252], [50, 2.89241], [51, 2.96748], [52, 3.03424], [53, 3.50271], [54, 4.03715], [55, 4.30524], [56, 4.38327], [57, 4.48275], [58, 4.55626], [59, 4.65751], [60, 4.73431], [61, 4.80021], [62, 4.89823], [63, 4.97422], [64, 5.06532], [65, 5.15623], [66, 5.21921], [67, 5.30028], [68, 5.34427],
    #  [42, 1.95757], [43, 2.10069], [44, 2.21937], [45, 2.33358], [46, 2.44328], [47, 2.82579], [48, 2.85471], [49, 2.89261], [50, 2.92358], [51, 2.96369], [52, 3.02418], [53, 3.05442], [54, 3.09478], [55, 3.13828], [56, 3.17862], [57, 3.22854], [58, 3.26835], [59, 3.29857], [60, 3.71364], [61, 3.74338], [62, 3.90083], [63, 3.94124], [64, 3.96386], [65, 3.99585], [66, 4.03897], [67, 4.08102], [68, 4.26213], [69, 4.30113], [70, 4.33716], [71, 4.36419], [72, 4.37718], [73, 4.47619], [74, 4.48719], [75, 4.53317], [76, 4.62217], [77, 4.70258], [78, 4.72253], [79, 4.74846], [80, 4.78735], [81, 4.8083], [82, 4.83622], [42, 1.97613], [43, 1.99708], [44, 2.04694], [45, 2.08036], [46, 2.13422], [47, 2.16214], [48, 2.80048], [49, 2.82941], [50, 2.85034], [51, 2.88326], [52, 2.90477], [53, 2.94488], [54, 2.9807], [55, 3.01092], [56, 3.0503], [57, 3.08154], [58, 3.12202], [59, 3.14521], [60, 3.18501], [61, 3.22539], [62, 3.26012], [63, 3.27525], [64, 3.29543], [65, 3.33401], [66, 3.35516], [67, 3.36523], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [42, 2.18487], [43, 2.41376], [44, 2.45764], [45, 2.50053], [46, 2.54991], [47, 2.6277], [48, 2.68655], [49, 2.7414], [50, 2.81023], [51, 2.99198], [52, 3.08267], [53, 3.15901], [54, 3.22404], [55, 3.37751], [56, 3.42591], [57, 3.48653], [58, 3.51925], [59, 3.5395], [60, 3.61388], [61, 3.64369], [62, 3.68903], [63, 3.73126], [64, 3.79992], [65, 3.88381], [66, 3.89083], [67, 3.93115], [68, 3.98214], [69, 3.98715], [55, 2.33323], [56, 2.35816], [57, 2.43495], [58, 2.4973], [59, 2.9414], [60, 3.47116], [61, 3.72916], [62, 3.80093], [63, 3.89126], [64, 3.95255], [65, 4.04473], [66, 4.14978], [67, 4.21782], [68, 4.33386], [69, 4.42688], [70, 4.51888], [71, 4.60888], [72, 4.68029], [73, 4.75708], [74, 4.78501], [75, 4.80296], [76, 4.88487], [77, 4.98488], [78, 5.10085], [79, 5.2029], [80, 5.26388], [81, 5.3819], [82, 5.45987], [83, 5.55194], [84, 5.62889], [85, 5.68689], [86, 5.77328], [87, 5.84608], [88, 5.95597], [89, 6.08594], [90, 6.16496], [91, 6.24593], [92, 6.28635], [93, 6.30604], [94, 6.38617], [95, 6.49424], [42, 3.21079], [43, 3.30152], [44, 3.65027], [45, 3.68573], [46, 3.7261], [47, 3.77656], [48, 3.81003], [49, 3.84727], [50, 3.88767], [51, 3.92351], [52, 3.98155], [53, 4.02567], [54, 4.07477], [55, 4.12776], [56, 4.16875], [57, 4.58037], [58, 4.61088], [59, 4.7401], [60, 4.78997], [61, 4.81889], [62, 4.84385], [63, 4.87584], [64, 4.90883], [65, 5.07484], [66, 5.11499], [67, 5.1489], [68, 5.18187], [69, 5.19089], [70, 5.27686], [71, 5.28684], [72, 5.34092], [73, 5.43386], [74, 5.52996], [75, 5.55192], [76, 5.56587], [77, 5.6009], [78, 5.62188], [79, 5.64987], [80, 5.67089], [81, 5.68985], [82, 5.72089], [68, 3.39246], [69, 3.43289], [70, 3.46561], [71, 4.05571], [72, 4.09029], [73, 4.11377], [74, 4.15975], [75, 4.17874], [76, 4.22031], [77, 4.24881], [78, 4.27482], [79, 4.33583], [80, 4.36586], [81, 4.39186], [82, 4.42036], [83, 4.44985], [84, 4.47986], [85, 4.52984], [86, 4.5509], [87, 4.57089], [88, 4.60187], [89, 4.62288], [90, 4.63886], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [69, 3.53651], [70, 3.78986], [71, 3.83515], [72, 3.8796], [73, 3.91992], [74, 4.05565], [75, 4.12268], [76, 4.19072], [77, 4.27873], [78, 4.45877], [79, 4.52177], [80, 4.59079], [81, 4.63925], [82, 4.75195], [83, 4.8058], [84, 4.86025], [85, 4.89475], [86, 4.91879], [87, 4.97276], [88, 5.02024], [89, 5.05973], [90, 5.09043], [91, 5.14977], [92, 5.20874], [93, 5.21575], [94, 5.26677], [95, 5.30873], [96, 5.31175], [97, 5.33181], [98, 5.38777], [99, 5.46875], [70, 4.03918], [71, 4.49551], [72, 4.99451], [73, 5.30148], [74, 5.37246], [75, 5.49852], [76, 5.57862], [77, 5.67951], [78, 5.75751], [79, 5.81891], [80, 5.91166], [81, 5.98858], [82, 6.09463], [83, 6.22057], [84, 6.28655], [85, 6.36871], [86, 6.39894], [87, 6.41564], [88, 6.50395], [89, 6.62569], [90, 6.7292], [91, 6.84392], [92, 7.19863], [93, 7.2249], [94, 7.27384], [95, 7.30568], [96, 7.37877], [97, 7.43873], [98, 7.48524], [99, 7.51757], [100, 7.55831], [101, 7.59895], [102, 7.6394], [103, 7.67981], [104, 7.72377], [105, 8.11386], [106, 8.17405], [107, 8.30526], [108, 8.35359], [109, 8.37577], [110, 8.39888], [42, 4.45843], [43, 4.49743], [44, 4.65776], [45, 4.68669], [46, 4.7196], [47, 4.74752], [48, 4.7565], [49, 4.83941], [50, 4.85292], [51, 4.89444], [52, 4.9794], [53, 5.06357], [54, 5.08152], [55, 5.09449], [56, 5.12045], [57, 5.14142], [58, 5.16442], [59, 5.18842], [60, 5.21742], [61, 5.2504], [62, 5.2814], [63, 5.31351], [64, 5.34645], [65, 5.91151], [66, 5.94952], [67, 5.97049], [68, 6.03351], [69, 6.06553], [70, 6.10149], [71, 6.13748], [72, 6.17047], [73, 6.20767], [74, 6.25407], [75, 6.2878], [76, 6.31758], [77, 6.34476], [78, 6.3752], [79, 6.40793], [80, 6.42808], [81, 6.44779], [82, 6.47765], [91, 4.66031], [92, 4.67527], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [93, 4.70619], [94, 4.94386], [95, 4.99784], [96, 5.03882], [97, 5.07683], [98, 5.16091], [99, 5.22485], [100, 5.29683], [101, 5.38386], [102, 5.52996], [103, 5.58885], [83, 4.90015], [84, 4.9582], [85, 5.07314], [86, 5.13532], [87, 5.18423], [88, 5.21519], [89, 5.23317], [90, 5.27817], [91, 5.31016], [92, 5.35015], [93, 5.39521], [94, 5.49818], [95, 5.56326], [96, 5.56924], [97, 5.61519], [98, 5.6572], [99, 5.66119], [100, 5.67818], [101, 5.70117], [102, 5.77861], [103, 5.83546], [104, 6.31872], [105, 6.86342], [106, 7.1441], [107, 7.21824], [108, 7.3383], [109, 7.39834], [110, 7.48522], [111, 7.56354], [112, 7.64343], [113, 7.74346], [114, 7.82348], [115, 7.91359], [116, 8.02362], [117, 8.14373], [118, 8.22456], [119, 8.25478], [120, 8.27494], [121, 8.36354], [122, 8.46396], [123, 8.56768], [69, 5.46134], [70, 5.82034], [71, 5.85031], [72, 5.89131], [73, 5.9383], [74, 5.97633], [75, 6.01629], [76, 6.0883], [77, 6.13227], [78, 6.17728], [79, 6.2177], [80, 6.25401], [81, 6.29438], [82, 6.32757], [83, 6.78255], [84, 6.82086], [85, 6.96734], [86, 7.01272], [87, 7.03292], [88, 7.07129], [89, 7.1127], [90, 7.16267], [91, 7.34584], [92, 7.38261], [93, 7.41657], [94, 7.4473], [95, 7.45745], [96, 7.54285], [97, 7.56866], [98, 7.61263], [99, 7.6978], [100, 7.77277], [101, 7.79038], [102, 7.80746], [103, 7.83274], [104, 7.85251], [105, 7.87765], [106, 7.90136], [107, 7.94274], [108, 7.98751], [109, 8.03259], [100, 5.5079], [101, 5.5448], [102, 6.13184], [103, 6.16783], [104, 6.19581], [105, 6.23182], [106, 6.25507], [107, 6.28937], [108, 6.32163], [109, 6.35492], [110, 6.38209], [111, 6.4105], [112, 6.43519], [113, 6.46541], [114, 6.50128], [115, 6.52507], [116, 6.57204], [117, 6.59424], [118, 6.6124], [119, 6.63459], [120, 6.65317], [121, 6.66547], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [104, 5.62188], [105, 5.88198], [106, 5.94097], [107, 5.98493], [108, 6.03593], [109, 6.14194], [110, 6.2079], [111, 6.27124], [112, 6.33523], [113, 6.49119], [114, 6.57407], [115, 6.64265], [116, 6.6957], [117, 6.82788], [118, 6.88647], [119, 6.96535], [120, 7.00976], [121, 7.02996], [122, 7.07519], [123, 7.11066], [124, 7.15112], [125, 7.17931], [126, 7.24492], [127, 7.30241], [128, 7.30492], [129, 7.34525], [130, 7.39325], [131, 7.4034], [132, 7.43362], [133, 7.46393], [134, 7.54531], [135, 7.61047], [83, 6.16044], [84, 6.68008], [85, 6.95003], [86, 7.03497], [87, 7.14907], [88, 7.22523], [89, 7.31498], [90, 7.38509], [91, 7.45529], [92, 7.55998], [93, 7.63426], [94, 7.73026], [95, 7.82782], [96, 7.88826], [97, 7.96698], [98, 8.0003], [99, 8.01739], [100, 8.10826], [101, 8.2153], [102, 8.32514], [103, 8.4167], [104, 8.74365], [105, 8.7705], [106, 8.80586], [107, 8.8302], [108, 8.85032], [109, 8.87711], [110, 8.91051], [111, 8.9302], [112, 8.95606], [113, 8.98018], [114, 9.00023], [115, 9.03014], [116, 9.06066], [117, 9.34056], [118, 9.36288], [119, 9.47002], [120, 9.49437], [121, 9.51251], [122, 9.52472], [123, 9.55012], [96, 6.53266], [97, 6.73508], [98, 6.76109], [99, 6.79131], [100, 6.84113], [101, 6.8512], [102, 6.95812], [103, 6.97149], [104, 7.02142], [105, 7.11169], [106, 7.20608], [107, 7.23285], [108, 7.25307], [109, 7.29132], [110, 7.32366], [111, 7.34628], [112, 7.36645], [113, 7.38612], [114, 7.42457], [115, 7.45632], [116, 7.50108], [117, 7.53621], [118, 8.14162], [119, 8.18212], [120, 8.20227], [121, 8.24052], [122, 8.26623], [123, 8.30098], [124, 8.33322], [125, 8.36139], [126, 8.38681], [127, 8.41174], [128, 8.43967], [129, 8.4656], [130, 8.49053], [131, 8.51846], [132, 8.55037], [133, 8.57132], [134, 8.59526], [135, 8.6172], [136, 8.63345], [83, 6.49279], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [84, 6.54276], [85, 6.79267], [86, 6.84258], [87, 6.89148], [88, 6.94771], [89, 7.04248], [90, 7.11777], [91, 7.19245], [92, 7.25498], [93, 7.4165], [94, 7.50295], [95, 7.58886], [122, 6.73003], [123, 6.87032], [124, 6.9268], [125, 7.00776], [126, 7.03492], [127, 7.05807], [128, 7.10057], [129, 7.14906], [130, 7.20505], [131, 7.25503], [132, 7.32058], [133, 7.375], [134, 7.38316], [135, 7.42353], [136, 7.46405], [137, 7.47007], [138, 7.48443], [139, 7.52002], [140, 7.59381], [141, 7.68027], [142, 8.15085], [143, 8.70325], [144, 8.90751], [145, 9.14817], [146, 9.17046], [147, 9.20025], [148, 9.22084], [149, 9.25008], [150, 9.27507], [151, 9.30185], [152, 9.33501], [153, 9.36285], [154, 9.39121], [155, 9.42004], [156, 9.44178], [157, 9.46399], [158, 9.70568], [159, 9.72576], [160, 9.81003], [161, 9.84033], [162, 9.84994], [136, 7.63629], [137, 7.69037], [138, 7.73026], [139, 7.91003], [140, 7.94527], [141, 7.99023], [142, 8.03751], [143, 8.04758], [144, 8.15888], [145, 8.17103], [146, 8.20927], [147, 8.27533], [148, 8.35533], [149, 8.37247], [150, 8.38778], [151, 8.41371], [152, 8.43665], [153, 8.46058], [154, 8.48252], [155, 8.50247], [156, 8.53538], [157, 8.55932], [158, 8.59423], [159, 8.62415], [160, 9.09806], [161, 9.12056], [162, 9.14036], [163, 9.16529], [164, 9.17855], [165, 9.20088], [166, 9.23094], [167, 9.25027], [168, 9.2715], [169, 9.29024], [170, 9.3099], [171, 9.33247], [172, 9.35277], [173, 9.37295], [174, 9.40333], [175, 9.41344], [176, 9.43367], [96, 7.61261], [97, 7.63283], [98, 7.64952], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [99, 7.69289], [100, 7.9428], [101, 8.01279], [102, 8.08257], [103, 8.13767], [104, 8.21777], [105, 8.28476], [106, 8.35132], [107, 8.41216], [108, 8.56575], [110, 8.10741], [111, 8.19255], [112, 8.24743], [113, 8.36105], [114, 8.42787], [115, 8.47773], [116, 8.51164], [117, 8.53358], [118, 8.5749], [119, 8.60765], [120, 8.64572], [121, 8.67399], [122, 8.73268], [123, 8.77918], [124, 8.7827], [125, 8.80748], [126, 8.84288], [127, 8.84797], [128, 8.86258], [129, 8.88292], [130, 8.94121], [131, 8.98265], [132, 9.29324], [133, 9.61287], [134, 9.77269]]
