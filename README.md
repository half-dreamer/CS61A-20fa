# CS61A学习总结

### 时间安排

​    学完CS61A的总时长大致为200h多一点

### 学习tips 

1. 学习顺序：reading-lecture-q&a-（lab/disc/hw)(顺序任意)-project ,个人建议如果不赶时间还是要把所有东西都学掉，如果非要砍掉一些内容，可以在disc（优先）或q&a选一个。非常不建议只看reading或只听lecture，reading读过一遍后其实印象不深，学习的逻辑性并不强，lecture不仅仅可以帮助捋顺课程逻辑，还可以通过代码演示加深对课程内容的理解。当然，大佬除外。

1. 版本选择：笔者选择的是20fa，一方面网上大部分的资源是以20fa为基础，其次是20fa的老师是John和Farid，John的语速以及吐字的清晰度对英语不佳的学习者十分友好，另一个讲师Farid的语速就稍微快点，用的高级词汇多一点，所以倒放的次数也多一点🤡

1. 课程设计极度用心，lab、hw、project都有相应的unblocker以保证理解题意，有非常多的hint video来提示、手把手教你写代码，这对初学者及其友善，但是过于丰富的资源在某种程度上会导致时间的浪费，所以在中后期阶段可以试着跳过一些hint video

1. 一道题不建议想过多的时间，如果不会就直接去看GitHub上其他人的solution或者官方的solution，非常非常非常建议看官方的solution，简洁，美观，有数学的韵味（笔者的GitHub上有官方的solution，链接放这里：[half-dreamer/CS61A-20fa](https://github.com/half-dreamer/CS61A-20fa)下的CS61A 2020 FALL all-solution

1. 由于使用的语言是Python，所以除了官方推荐的vscode，Pycharm也可以试试，但由于一直找不到喜欢的IDE theme，所以lz就放弃使用Pycharm了🤡；同时使用Pycharm有一定的学习成本，所以还是建议使用vscode

1. 由于是个人刷课，所以经常需要面向Google，Stack Overflow学习，当然Python的菜鸟教程也很好，可以在正式学习61a前花几个小时过一遍菜鸟，可以大致了解Python的语法

1. 其实对于很多人提倡的组队刷课的方式，我个人不是很建议，每个人的速度都不一样，遇到的bug也不一而陈，对于初学者，很多的问题可以直接Google一下就会解决，当然交流也很重要，所以可以加一下61a的学习交流群（知乎搜一下），群里人比较多，愿意解答的大佬也很多

1. 建议用英文学习，不建议直接去b站找翻译字幕或找中文翻译版的教材，一方面做的作业都是英文描述，用英文学习可以提高自己的解题能力，尤其是刚开始的时候可能会有很多的单词不认识，但还是建议尝试克服；另一方面英文的资源更加丰富，csdn或多或少比不过Stack Overflow，有些名词翻译过来多多少少有点奇怪，英文的话就更加自然一点

### 学习感想

1. 学习了61a后很困惑，以浙大的教育质量，是凭什么在QS榜上挤进前五十，甚至还比CMU高（乐中乐）

2. 61a的教材浅显易懂，即使是英文也并不晦涩，上课的进度也基本按照教材的内容推进，学习进度更容易把握，反观像极了出版社催稿、一周赶工完成的线代教材，内容随机分布，定理随意出现，全书不提几何，令人喟叹，读完这种书需要多大的毅力😇。

3. UCB的老师十分和蔼，亲切甚至于说可爱（在John的Youtube主页上还能看到他和妻子的甜蜜日常🥰），lecture上各种的joke让学习不那么乏味，两个教授之间也经常打趣，自由、轻松、活跃的学习氛围实在是让人心驰神往

4. 另一个比较印象深刻的点，discussion课上John和Farid很明显是基本没什么准备的，Farid也经常会想到什么问题就说什么问题，向John提问。我估摸着在折大应该是没有这种情况的，毕竟有些老师被问倒的情况还是时有发生的😇（想起了计概的jxh女士🥰）

5. 61a可以让学习者感受到数学的美感，就像John强调的generic（不知道怎么翻译，可能是普遍化？）的思想，和数学中探寻普遍定理的思想非常接近，在某种程度上个人认为是代码美感的主要来源。就像对称是美的，把个例普遍化，精简化同样是十分有艺术感的过程。所以我一直觉得以代码量来评分不是个很好的行为，毕竟如果想凑一个冗长的代码，只需要不断Ctrl-C + Ctrl-V来实现本质没什么不同的功能。

6. 作为一个理工类课程，61a的艺术性又无处不在。“for the sake of art“ John常常提及，61a的网站设置也很漂亮。同时，61a的作业有很多和艺术相关。比如scheme相关作业有画画创作，每一年的作品都在课程网站上，比如[Scheme Art Gallery | CS 61A Fall 2020 (berkeley.edu)](https://inst.eecs.berkeley.edu/~cs61a/fa20/proj/scheme_gallery/)

   当22年的我回看20fa UCB学生的创作时，突然有一丝触动，让我回到了那个曾经疫情爆发的时期，这是其中一个学生所作：

   ![img](https://inst.eecs.berkeley.edu//~cs61a/su20/proj/scheme_gallery/entries/23b998b1/artwork.png)

   > 作品名：Dubai
   >
   >  注脚：Stuck at home this fall;
   > 			I'm 8000 miles from Cal.
   > 			Sunset's quite nice though.

7. 61a的有一个optional的lecture   Ethical Al&Data，非常严肃地探讨了AI在现实生活中的应用以及面临的道德问题，并不是蜻蜓点水般站在道德高地，大笔一挥，无关痛痒地讲两句，而是用教授Farid自己做的实际的Al模型应用种族犯罪的事例去设身处地、满怀人文关怀地探讨。就像Farid所说的，如果AI任何一个可能出现的bug，一点偏差会导致一个人身陷囹圄，那AI的应用就仍然需要斟酌，如果那个因为AI而被冤枉的人是你或者你的亲人，你会作何感想？上完这节课后，我对UCB突然有了非常崇高的敬意，他们是真正地在change the world，他们是在以世界改造者的身份自我反思，我想，如果任何一个学生在刚接触computer science的时候能有人指引正确的方向，有人愿意和他去探讨科技的利弊，有人告诉他：what you are doing might change the world，世界或许会变得更好。由于笔者文字水平太烂无法表述出上过此课后震撼的感觉，所以感兴趣的同学可以自己观看[61A Fall 2020 Lecture 26 Video ](https://www.youtube.com/watch?v=6F04tADaeMs&list=PL6BsET-8jgYV2CEjAGz5Fbu68cmMxWDqb)

8. Anyway，无论是谁，我都很建议去看看真正该有的大学课程的样子，从高中到大学，我想大部分同学接受的教育质量都会有断崖的下滑，高中时老师们精心准备每一节课，每一个知识点都切碎了给你，选择的教辅也必然是年级组仔细考量的，无论高考教的东西是否有用，高中老师们在高考上的建树一定是丰厚的；而大学呢，大多数课都有时代的烙印，比如某个实训课一定要使用早已被淘汰的远古版本的AutoCAD，比如祖传的陈年PPT



### 鸣谢

​     笔者在学习前参考了一些前辈的帖子，感谢巨人的肩膀

​     [ CS61A 学习经验&感想 ](https://www.cc98.org/topic/5280441)

​      [分享一下自己自学两个月CS61A的情况 ](https://www.cc98.org/topic/4909055)

​      感谢@HobbitQia 同学的GitHub以及提供的帮助



### 尾声

最后，以UCB的校训做结


> Let There Be Light

UCB不仅把光照到了她的学生的道路上，也把取光的机会慷慨地放到了公众面前

顾城写过一个很美的诗句

> 黑夜给了我黑色的眼睛，我却用它寻找光明

与诸君共勉
