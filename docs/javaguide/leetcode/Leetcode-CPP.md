---
title: Leetcode-CPP
source: JavaGuide/LeetCode/Leetcode-CPP.pdf
pages: 262
converted_at: 2026-06-22 22:30:12
---

# Leetcode-CPP

LeetCode 题解
▤偱ᱩ஗(soulmachine@gmail.com)
https://github.com/soulmachine/leetcode
ᰯऽᰣ᫟2016-1-28
❷ᱲฟᬽ
ᱛҋৰ䛶⩗ĆCreative Commons 㒡़-䲍ੵ͉ᕖҮ⩗-Ⱗऻ᫨ᐾڠϚ 3.0 Unported 䃧ञࡾ䃝
(cc by-nc-sa)ć䔊㵻䃧ञȡhttp://creativecommons.org/licenses/by-nc-sa/3.0/
ڴშクϺ
ᱛΕ⮳Ⱍᴶ䄪㔴᭞۵ึ࣪ࡆ㒽ឭጔҋ⮳ⴰۋ喌Ύ䔱⩗ν౗బڴឭጔҋ⮳ⴰۋ喌Дࣹ݉
ᣔ㼕ACM テ∄」䊊⮳᫟᝺ȡ
ᱛΕ࠴ग़ε LeetCode Online Judge(http://leetcode.com/onlinejudge) ᝯ᰸题Ⱍ⮳ゃᵷ喌ᝯ᰸
Вⴰ㏾䓶㇭ᓲ㑅ۈ喌㑅ⴰ㻳㠲㞞ຬ喌䔱ष䄪㔴ࣼ฼ᤒᦘ喌ὐЮ喌⩉㜢౗㏧̹吇ۈȡ
ڗΕ⮳Вⴰ喌Ү⩗C++ 11 ⮳㑅ۈ喌Ꭵ౗LeetCode Online Judge ̹≺䄄䕉䓶ȡᱛΕ͜⮳
Вⴰ㻳㠲喌䌎౗ڛध͜⮳ጔ⼺㻳㠲⪔᰸̼ऻ喌ͩεҮВⴰⴜ喈᫨Ӯ䓴䕎Ⴭ⣟喉:
• ᝯ᰸Вⴰ䘬᭞ࢄ̯᪶Хȡ䔈᭞ఏ̯ͩ㝛OJ 㒀〈喌᣿ϓВⴰ⮳ᬥՈङ᰸̯͙᪶ᱛᵵ喌ັ
᳋䔇᭞ᠸ⚖ᴶ۵։∄喌℃ັܵͩ๣᪶Х.h ঻⎿Вⴰ.cpp喌ᬏ∄౗㒀〈̹᣿ϓ喛
• Shorter is betterȡ㘬䕁ᒁ݈̯჉̼⩗ᴷ喛㘬⩗STL ݈̯჉̼㜙ጠჍ⣟ȡ
• ̼᣿Ր䭡ᓐᐾ㑅⼺ȡ̼䰯㺰ᷯᴔmalloc()/new 䔃఍⮳ᠶ䦷᭞ॕͩ nullptr喛̼䰯㺰ᷯᴔ
ڴ䘗ܬ᪟ڔऒࣱ᪟⮳᰸᩷ᕖȡ
ᱛ᝺ڻն჉䄪㔴ጡ㏾႕䓶Ȩ᪟ᢝ㐂Ჳȩx喌Ȩテ∄ȩy 䔈͓䬗䄭喌⛎㏲ᢻᤐC++ ᝅJavaȡ
GitHub ౟౯
ᱛΕ᭞ᐯ⎿⮳喌GitHub ౟౯喚https://github.com/soulmachine/leetcode
ࡆ㒽ⅱ㕻ᓝࢉ㓓
ᝀ঻ᝀ⮳ᄾшѣЛ౗䔈䛻喚http://q.weibo.com/1312378
xȨ᪟ᢝ㐂Ჳȩ喌͔㩉᩾へ㦆喌⌴ࡽ๖႕ܩ❷⹭喌http://book.douban.com/subject/2024655/
yȨAlgorithmsȩ喌Robert Sedgewick, Addison-Wesley Professional, http://book.douban.com/subject/4854123/
i

---

Ⱍᒄ
せ1 』㑅⼺ឯ጖
1
せ2 』㏮ᕖ㶗
2
2.1
᪟㏳. . . . . . . . . . . . . . .
2
2.1.1
Remove
Duplicates
from Sorted Array
. . .
2
2.1.2
Remove
Duplicates
from Sorted Array II . .
3
2.1.3
Search
in
Rotated
Sorted Array
. . . . . .
5
2.1.4
Search
in
Rotated
Sorted Array II . . . . .
6
2.1.5
Median of Two Sorted
Arrays . . . . . . . . . .
7
2.1.6
Longest
Consecutive
Sequence . . . . . . . .
8
2.1.7
Two Sum . . . . . . . .
10
2.1.8
3Sum . . . . . . . . . .
12
2.1.9
3Sum Closest . . . . . .
13
2.1.10 4Sum . . . . . . . . . .
14
2.1.11 Remove Element . . . .
18
2.1.12 Next Permutation . . . .
19
2.1.13 Permutation Sequence .
21
2.1.14 Valid Sudoku . . . . . .
23
2.1.15 Trapping Rain Water . .
24
2.1.16 Rotate Image . . . . . .
27
2.1.17 Plus One
. . . . . . . .
28
2.1.18 Climbing Stairs . . . . .
30
2.1.19 Gray Code
. . . . . . .
31
2.1.20 Set Matrix Zeroes . . . .
33
2.1.21 Gas Station . . . . . . .
35
2.1.22 Candy . . . . . . . . . .
36
2.1.23 Single Number . . . . .
37
2.1.24 Single Number II . . . .
38
2.2
ࢄ䨭㶗
. . . . . . . . . . . . .
40
2.2.1
Add Two Numbers . . .
40
2.2.2
Reverse Linked List II .
41
2.2.3
Partition List . . . . . .
42
2.2.4
Remove
Duplicates
from Sorted List
. . . .
43
2.2.5
Remove
Duplicates
from Sorted List II . . .
44
2.2.6
Rotate List
. . . . . . .
46
2.2.7
Remove
Nth
Node
From End of List . . . .
47
2.2.8
Swap Nodes in Pairs . .
47
2.2.9
Reverse Nodes in k-Group 49
2.2.10 Copy List with Random
Pointer
. . . . . . . . .
50
2.2.11 Linked List Cycle . . . .
51
2.2.12 Linked List Cycle II
. .
52
2.2.13 Reorder List
. . . . . .
53
2.2.14 LRU Cache . . . . . . .
55
せ3 』ႆさ͡
57
3.1
Valid Palindrome . . . . . . . .
57
3.2
Implement strStr() . . . . . . . .
58
3.3
String to Integer (atoi)
. . . . .
60
ii

---

Ⱍᒄ
iii
3.4
Add Binary . . . . . . . . . . .
61
3.5
Longest Palindromic Substring .
62
3.6
Regular Expression Matching . .
66
3.7
Wildcard Matching . . . . . . .
67
3.8
Longest Common Prefix
. . . .
69
3.9
Valid Number . . . . . . . . . .
70
3.10 Integer to Roman . . . . . . . .
72
3.11 Roman to Integer . . . . . . . .
73
3.12 Count and Say . . . . . . . . . .
74
3.13 Anagrams . . . . . . . . . . . .
75
3.14 Simplify Path . . . . . . . . . .
76
3.15 Length of Last Word
. . . . . .
77
せ4 』ᴷ঻䭎݆
79
4.1
ᴷ. . . . . . . . . . . . . . . .
79
4.1.1
Valid Parentheses . . . .
79
4.1.2
Longest Valid Paren-
theses . . . . . . . . . .
80
4.1.3
Largest
Rectangle
in
Histogram . . . . . . . .
82
4.1.4
Evaluate Reverse Pol-
ish Notation . . . . . . .
84
4.2
䭎݆. . . . . . . . . . . . . . .
85
せ5 』ᵀ
86
5.1
λࣸᵀ⮳䕼ࢵ
. . . . . . . . .
86
5.1.1
Binary Tree Preorder
Traversal . . . . . . . .
86
5.1.2
Binary
Tree
Inorder
Traversal . . . . . . . .
88
5.1.3
Binary Tree Postorder
Traversal . . . . . . . .
90
5.1.4
Binary Tree Level Or-
der Traversal . . . . . .
92
5.1.5
Binary Tree Level Or-
der Traversal II . . . . .
94
5.1.6
Binary
Tree
Zigzag
Level Order Traversal
.
96
5.1.7
Recover Binary Search
Tree . . . . . . . . . . .
98
5.1.8
Same Tree
. . . . . . .
99
5.1.9
Symmetric Tree . . . . . 100
5.1.10 Balanced Binary Tree . . 102
5.1.11 Flatten Binary Tree to
Linked List . . . . . . . 103
5.1.12 Populating Next Right
Pointers in Each Node II 105
5.2
λࣸᵀ⮳Ჳᐩ
. . . . . . . . . 106
5.2.1
Construct Binary Tree
from Preorder and In-
order Traversal . . . . . 106
5.2.2
Construct Binary Tree
from Inorder and Pos-
torder Traversal . . . . . 107
5.3
λࣸᴔឭᵀ. . . . . . . . . . . 108
5.3.1
Unique Binary Search
Trees
. . . . . . . . . . 108
5.3.2
Unique Binary Search
Trees II . . . . . . . . . 110
5.3.3
Validate Binary Search
Tree . . . . . . . . . . . 111
5.3.4
Convert Sorted Array to
Binary Search Tree . . . 112
5.3.5
Convert Sorted List to
Binary Search Tree . . . 113
5.4
λࣸᵀ⮳䕁ᒁ
. . . . . . . . . 114
5.4.1
Minimum Depth of Bi-
nary Tree . . . . . . . . 115

---

iv
Ⱍᒄ
5.4.2
Maximum Depth of Bi-
nary Tree . . . . . . . . 116
5.4.3
Path Sum . . . . . . . . 117
5.4.4
Path Sum II . . . . . . . 118
5.4.5
Binary Tree Maximum
Path Sum . . . . . . . . 119
5.4.6
Populating Next Right
Pointers in Each Node . 120
5.4.7
Sum Root to Leaf Num-
bers . . . . . . . . . . . 121
せ6 』ᣁᎾ
123
6.1
Merge Sorted Array . . . . . . . 123
6.2
Merge Two Sorted Lists . . . . . 124
6.3
Merge k Sorted Lists
. . . . . . 124
6.4
Insertion Sort List . . . . . . . . 125
6.5
Sort List . . . . . . . . . . . . . 126
6.6
First Missing Positive . . . . . . 127
6.7
Sort Colors
. . . . . . . . . . . 128
せ7 』ᴔឭ
131
7.1
Search for a Range
. . . . . . . 131
7.2
Search Insert Position . . . . . . 132
7.3
Search a 2D Matrix . . . . . . . 133
せ8 』ᯣߊ᳉ͭ∄
135
8.1
Subsets
. . . . . . . . . . . . . 135
8.1.1
䕁ᒁ
. . . . . . . . . . 135
8.1.2
䔜В
. . . . . . . . . . 137
8.2
Subsets II . . . . . . . . . . . . 138
8.2.1
䕁ᒁ
. . . . . . . . . . 138
8.2.2
䔜В
. . . . . . . . . . 141
8.3
Permutations
. . . . . . . . . . 142
8.3.1
next_permutation() . . . 142
8.3.2
䛼᫟Ⴭ⣟next_permu-
tation()
. . . . . . . . . 142
8.3.3
䕁ᒁ
. . . . . . . . . . 143
8.4
Permutations II . . . . . . . . . 144
8.4.1
next_permutation() . . . 144
8.4.2
䛼᫟Ⴭ⣟next_permu-
tation()
. . . . . . . . . 144
8.4.3
䕁ᒁ
. . . . . . . . . . 144
8.5
Combinations . . . . . . . . . . 146
8.5.1
䕁ᒁ
. . . . . . . . . . 146
8.5.2
䔜В
. . . . . . . . . . 147
8.6
Letter Combinations of a Phone
Number . . . . . . . . . . . . . 147
8.6.1
䕁ᒁ
. . . . . . . . . . 148
8.6.2
䔜В
. . . . . . . . . . 149
せ9 』ᎮᏕчٷ᥋㉑
150
9.1
Word Ladder
. . . . . . . . . . 150
9.2
Word Ladder II . . . . . . . . . 154
9.3
Surrounded Regions . . . . . . . 162
9.4
ᄾ㐂. . . . . . . . . . . . . . . 164
9.4.1
䔱⩗౩ᮞ. . . . . . . . 164
9.4.2
ᕌ㔲⮳ₔ俓
. . . . . . 164
9.4.3
ВⴰὐᲮ. . . . . . . . 165
せ10 』⌠Ꮥчٷ᥋㉑
173
10.1 Palindrome Partitioning . . . . . 173
10.2 Unique Paths
. . . . . . . . . . 176
10.2.1 ⌠᥋
. . . . . . . . . . 176
10.2.2 ึᔇᒄ∄. . . . . . . . 176
10.2.3 ߗ㻳
. . . . . . . . . . 177
10.2.4 ᪟႕ڛᐾ. . . . . . . . 178
10.3 Unique Paths II . . . . . . . . . 179
10.3.1 ึᔇᒄ∄. . . . . . . . 179
10.3.2 ߗ㻳
. . . . . . . . . . 180

---

Ⱍᒄ
v
10.4 N-Queens . . . . . . . . . . . . 181
10.5 N-Queens II . . . . . . . . . . . 184
10.6 Restore IP Addresses . . . . . . 186
10.7 Combination Sum . . . . . . . . 188
10.8 Combination Sum II
. . . . . . 189
10.9 Generate Parentheses . . . . . . 190
10.10 Sudoku Solver . . . . . . . . . 192
10.11 Word Search . . . . . . . . . . 193
10.12 ᄾ㐂. . . . . . . . . . . . . . 195
10.12.1 䔱⩗౩ᮞ
. . . . . . . 195
10.12.2 ᕌ㔲⮳ₔ俓. . . . . . 195
10.12.3 ВⴰὐᲮ
. . . . . . . 197
10.12.4 ⌠᥋̽఍⏞∄⮳ࡩݚ. 197
10.12.5 ⌠᥋̽䕁ᒁ⮳ࡩݚ. . 197
せ11 』
ܵ⇪∄
199
11.1 Pow(x,n) . . . . . . . . . . . . . 199
11.2 Sqrt(x) . . . . . . . . . . . . . . 200
せ12 』
䉙ᓲ∄
201
12.1 Jump Game . . . . . . . . . . . 201
12.2 Jump Game II . . . . . . . . . . 202
12.3 Best Time to Buy and Sell Stock 204
12.4 Best Time to Buy and Sell Stock II205
12.5 Longest Substring Without Re-
peating Characters
. . . . . . . 206
12.6 Container With Most Water . . . 207
せ13 』
ߗᔰ㻳݁
209
13.1 Triangle . . . . . . . . . . . . . 209
13.2 Maximum Subarray . . . . . . . 210
13.3 Palindrome Partitioning II
. . . 212
13.4 Maximal Rectangle . . . . . . . 213
13.5 Best Time to Buy and Sell Stock
III . . . . . . . . . . . . . . . . 214
13.6 Interleaving String
. . . . . . . 215
13.7 Scramble String . . . . . . . . . 217
13.8 Minimum Path Sum . . . . . . . 222
13.9 Edit Distance . . . . . . . . . . 224
13.10 Decode Ways
. . . . . . . . . 226
13.11 Distinct Subsequences . . . . . 227
13.12 Word Break
. . . . . . . . . . 228
13.13 Word Break II . . . . . . . . . 230
せ14 』భ
232
14.1 Clone Graph . . . . . . . . . . . 232
せ15 』㏵㞱Ⴭ⣟题
235
15.1 Reverse Integer . . . . . . . . . 235
15.2 Palindrome Number . . . . . . . 236
15.3 Insert Interval . . . . . . . . . . 237
15.4 Merge Intervals . . . . . . . . . 238
15.5 Minimum Window Substring . . 239
15.6 Multiply Strings . . . . . . . . . 241
15.7 Substring with Concatenation
of All Words . . . . . . . . . . . 244
15.8 Pascal’s Triangle
. . . . . . . . 245
15.9 Pascal’s Triangle II . . . . . . . 246
15.10 Spiral Matrix . . . . . . . . . . 247
15.11 Spiral Matrix II . . . . . . . . . 248
15.12 ZigZag Conversion
. . . . . . 250
15.13 Divide Two Integers . . . . . . 251
15.14 Text Justification . . . . . . . . 253
15.15 Max Points on a Line
. . . . . 255

---

vi
Ⱍᒄ

---

せ1 』
㑅⼺ឯ጖
౗ݓ᫜͓͙⊝◨᪟a ঻b ᭞ॕⰧへᬥ喌̼㺰⩗a==b喌Ꮓ䄔ݓ᫜λ㔴ͺጝ⮳㐌ᄨի
fabs(a-b) ᭞ॕᄾν᳿͙䬷ի喌Һັ1e-9ȡ
ݓ᫜̯͙᪣᪟᭞ॕ᭞ͩ๶᪟喌⩗x % 2 != 0喌̼㺰⩗x % 2 == 1喌ఏͩ x ञ㘬᭞䉎
᪟ȡ
⩗char ⮳իҋͩ᪟㏳̺ᴶ喈Һັ喌㐎䃐ႆさ͜͡⃾͙ႆさܩ⣟⮳⁐᪟喉喌㺰㔲㮀ݟ
char ञ㘬᭞䉎᪟ȡ᰸⮳ϩ㔲㮀ݟε喌ٷᑩݥ䒛಺ͩ unsigned int ڼ⩗ҋ̺ᴶ喌䔈ϼ♥᭞
䩈⮳ȡₒ⶝⮳։∄᭞喌ٷᑩݥ䒛಺ͩ unsigned char喌ڼ⩗ҋ̺ᴶȡ䔈⊸ࣹC++ ᪣಺᣿ࡶ
⮳㻳݈喌ᅠ̼䄕䔟εȡ
Д̺᭞ڢν STL Ү⩗ឯ጖⮳喌ᒷ้Ა⁭Ე㜙ȨEffective STLȩ䔈ᱛΕȡ
vector ঻string чٷνߗᔰܵ䙼⮳᪟㏳
仅ٷ喌౗ᕖ㘬̹喌⩠ν vector 㘬๎Ԍ䃰䔍㐜ڴႇ喌ఏₓ̯ᬕܵ䙼εऽ喌Ⴒ⮳ᕖ㘬䌎
࣎໺᪟㏳Ⱗᒂ喛
ڥ⁐喌ັ᳋⩗new喌ᘾঢⱯҏ㺰⶝Ԍऽ䲑䔊㵻ε delete喌̯ᬕᔇ䃟ε喌ᅠщܩ⣟BUG喌
̓䔈ᵦ䰯㺰䘬ۈ̯㵻delete喌Вⴰ̼๎ⴜ喛
ڼ⁐喌ฟᬽ้㐣᪟㏳⮳䄌喌ङ㘬̯͙̯͙ new喌Һັ喚
int** ary = new int*[row_num];
for(int i = 0; i < row_num; ++i)
ary[i] = new int[col_num];
⩗vector ⮳䄌̯㵻Вⴰ᥍჉喌
vector<vector<int> > ary(row_num, vector<int>(col_num, 0));
Ү⩗reserve Ე䖮ټ̼ᓴ㺰⮳䛼᫟ܵ䙼
1

---

せ2 』
㏮ᕖ㶗
䔈ㆪ题Ⱍ㔲ᄎ㏮ᕖ㶗⮳᧼ҋ喌Һັ喌᪟㏳喌ࢄ䨭㶗喌ࣻी䨭㶗へȡ
2.1
᪟㏳
2.1.1
Remove Duplicates from Sorted Array
᣾䔟
Given a sorted array, remove the duplicates in place such that each element appear only once
and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
ܵᲿ
ᬏ
Вⴰ1
// LeetCode, Remove Duplicates from Sorted Array
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int removeDuplicates(vector<int>& nums) {
if (nums.empty()) return 0;
int index = 0;
for (int i = 1; i < nums.size(); i++) {
if (nums[index] != nums[i])
nums[++index] = nums[i];
}
return index + 1;
}
};
2

---

2.1
᪟㏳
3
Вⴰ2
// LeetCode, Remove Duplicates from Sorted Array
// Ү⩗STL喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int removeDuplicates(vector<int>& nums) {
return distance(nums.begin(), unique(nums.begin(), nums.end()));
}
};
Вⴰ3
// LeetCode, Remove Duplicates from Sorted Array
// Ү⩗STL喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int removeDuplicates(vector<int>& nums) {
return distance(nums.begin(), removeDuplicates(nums.begin(), nums.end(), nums.begin())
}
template<typename InIt, typename OutIt>
OutIt removeDuplicates(InIt first, InIt last, OutIt output) {
while (first != last) {
*output++ = *first;
first = upper_bound(first, last, *first);
}
return output;
}
};
Ⱗڢ题Ⱍ
• Remove Duplicates from Sorted Array II喌㻰§2.1.2
2.1.2
Remove Duplicates from Sorted Array II
᣾䔟
Follow up for ”Remove Duplicates”: What if duplicates are allowed at most twice?
For example, Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3]
ܵᲿ
ߏ̯͙इ䛾䃟ᒄ̯̺ٲ㉏ܩ⣟⮳⁐᪟ࢢञȡ䔈题ఏͩ᭞ጡ㏾ᣁᎾ⮳᪟㏳喌ᝯД̯͙इ䛾ࢢञ解
ۢȡັ᳋᭞⇐᰸ᣁᎾ⮳᪟㏳喌݈䰯㺰ᑄڔ̯͙ hashmap Ე䃟ᒄܩ⣟⁐᪟ȡ

---

4
せ2 』
㏮ᕖ㶗
Вⴰ1
// LeetCode, Remove Duplicates from Sorted Array II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
// @author hex108 (https://github.com/hex108)
class Solution {
public:
int removeDuplicates(vector<int>& nums) {
if (nums.size() <= 2) return nums.size();
int index = 2;
for (int i = 2; i < nums.size(); i++){
if (nums[i] != nums[index - 2])
nums[index++] = nums[i];
}
return index;
}
};
Вⴰ2
̺䲑᭞̯͙ᰣク∰⮳❷ᱛȡ̹䲑⮳Вⴰ⪔䪮喌̼䓶មᆄᕖຬ̯ϊ喌Һັᄵoccur < 2 ᩨͩ occur
< 3喌ᅠइ᜿εٰ䃧䛼฼ᰯ้3 ⁐ȡ
// LeetCode, Remove Duplicates from Sorted Array II
// @author 㮍㝙С (http://weibo.com/u/1666779725)
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int removeDuplicates(vector<int>& nums) {
const int n = nums.size();
int index = 0;
for (int i = 0; i < n; ++i) {
if (i > 0 && i < n - 1 && nums[i] == nums[i - 1] && nums[i] == nums[i + 1])
continue;
nums[index++] = nums[i];
}
return index;
}
};
Ⱗڢ题Ⱍ
• Remove Duplicates from Sorted Array喌㻰§2.1.1

---

2.1
᪟㏳
5
2.1.3
Search in Rotated Sorted Array
᣾䔟
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
ܵᲿ
λܵᴔឭ喌䯭Ꮥͪ㺰౗νጕढ䓨⩻⮳⶝჉ȡ
Вⴰ
// LeetCode, Search in Rotated Sorted Array
// ᬥ䬣฼ᱱᏕO(log n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int search(const vector<int>& nums, int target) {
int first = 0, last = nums.size();
while (first != last) {
const int mid = first
+ (last - first) / 2;
if (nums[mid] == target)
return mid;
if (nums[first] <= nums[mid]) {
if (nums[first] <= target && target < nums[mid])
last = mid;
else
first = mid + 1;
} else {
if (nums[mid] < target && target <= nums[last-1])
first = mid + 1;
else
last = mid;
}
}
return -1;
}
};
Ⱗڢ题Ⱍ
• Search in Rotated Sorted Array II喌㻰§2.1.4

---

6
せ2 』
㏮ᕖ㶗
2.1.4
Search in Rotated Sorted Array II
᣾䔟
Follow up for ”Search in Rotated Sorted Array”: What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
ܵᲿ
ٰ䃧䛼฼ٲ㉏喌݈̹̯题͜ັ᳋A[m]>=A[l], 䗒ͷ [l,m] ͩ䕁෍Ꮎ݆⮳ն䃭ᅠ̼㘬᜿⿺ε喌℃
ັ[1,3,1,1,1]ȡ
ັ᳋A[m]>=A[l] ̼㘬⶝჉䕁෍喌䗒ᅠឹႲ៵ܵ᜿͓͙ᲐХ喚
• 㠔A[m]>A[l]喌݈ࡩ䬣[l,m] ̯჉䕁෍
• 㠔A[m]==A[l] ⶝჉̼ε喌䗒ᅠl++喌ᒯ̺ⰺ̯ₔࢢञȡ
Вⴰ
// LeetCode, Search in Rotated Sorted Array II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool search(const vector<int>& nums, int target) {
int first = 0, last = nums.size();
while (first != last) {
const int mid = first
+ (last - first) / 2;
if (nums[mid] == target)
return true;
if (nums[first] < nums[mid]) {
if (nums[first] <= target && target < nums[mid])
last = mid;
else
first = mid + 1;
} else if (nums[first] > nums[mid]) {
if (nums[mid] < target && target <= nums[last-1])
first = mid + 1;
else
last = mid;
} else
//skip duplicate one
first++;
}
return false;
}
};

---

2.1
᪟㏳
7
Ⱗڢ题Ⱍ
• Search in Rotated Sorted Array喌㻰§2.1.3
2.1.5
Median of Two Sorted Arrays
᣾䔟
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted
arrays. The overall run time complexity should be O(log(m + n)).
ܵᲿ
䔈᭞̯䖂䲍፧㏾ڧ⮳题ȡ䔈题ᰣ䕉⩗⮳ᒑᐾ᭞喌㐈჉͓͙ጡ㏾ᣁᎾຬ⮳᪟㏳喌ឭݟ͓㔴ᝯ᰸ٲ
㉏͜せk ๖⮳ٲ㉏ȡ
O(m + n) ⮳解∄℃䒲Ⱓ㻱喌Ⱓᣔmerge ͓͙᪟㏳喌♥ऽⅱせk ๖⮳ٲ㉏ȡ
̼䓶ᝀЛϴϴ䰯㺰せk ๖⮳ٲ㉏喌᭞̼䰯㺰ĆᣁᎾć䔈ͷᬱ䉤⮳᧼ҋ⮳ȡञД⩗̯͙䃐᪟஗喌䃟
ᒄᒂݼጡ㏾ឭݟせm ๖⮳ٲ㉏εȡऻᬥᝀЛҮ⩗͓͙ᠶ䦷pA ঻pB喌ܵݚᠶीA ঻B ᪟㏳⮳せ̯
͙ٲ㉏喌Ү⩗ㆪѫν merge sort ⮳࣎⤵喌ັ᳋᪟㏳A ᒂݼٲ㉏ᄾ喌䗒ͷ pA++喌ऻᬥm++喛ັ᳋᪟㏳
B ᒂݼٲ㉏ᄾ喌䗒ͷ pB++喌ऻᬥm++ȡᰯ㏷ᒂm へν k ⮳ᬥՈ喌ᅠᓆݟεᝀЛ⮳ゃᵷ喌O(k) ᬥ䬣喌
O(1) ⾩䬣ȡѵ᭞喌ᒂk ᒷᣔ䔀m + n ⮳ᬥՈ喌䔈͙᫨∄䔇᭞O(m + n) ⮳ȡ
᰸⇐᰸ᰣຬ⮳᫨ᵷ঑喟ᝀЛञД㔲㮀Ͻ k ڔ᝺ȡັ᳋ᝀЛ⃾⁐䘬㘬๎ݏ䮓̯͙̯჉౗せk ๖ٲ
㉏ͺݼ⮳ٲ㉏喌䗒ͷᝀЛ䰯㺰䔊㵻k ⁐ȡѵ᭞ັ᳋⃾⁐ᝀЛ䘬ݏ䮓̯ࡹ঑喟⩠ν A ঻B 䘬᭞᰸Ꮎ⮳喌
ᝀЛᏃ䄔ٴܵݘ⩗䔈䛻䲑⮳Ԑᖞ喌ㆪѫνλܵᴔឭ喌Ύ᭞ٴܵݘ⩗εĆ᰸Ꮎćȡ
ն䃭A ঻B ⮳ٲ㉏͙᪟䘬๖ν k/2喌ᝀЛᄵA ⮳せk/2 ͙ٲ㉏喈ࢢA[k/2-1]喉঻B ⮳せk/2
͙ٲ㉏喈ࢢB[k/2-1]喉䔊㵻℃䒲喌᰸Д̸̺⻼ᗴۤ喈ͩεクࡅ䔈䛻ٷն䃭k ֥ͩ᪟喌ᝯᓆݟ⮳㐂䃩
ᄨν k ᭞๶᪟Ύ᭞᜿⿺⮳喉喚
• A[k/2-1] == B[k/2-1]
• A[k/2-1] > B[k/2-1]
• A[k/2-1] < B[k/2-1]
ັ᳋A[k/2-1] < B[k/2-1]喌ᘾঢⱯA[0] ݟA[k/2-1] ⮳㗞჉౗A ∪B ⮳top k ٲ㉏⮳㠲ణ
ڴ喌ᢑऔ䄌䄣喌A[k/2-1] ̼ञ㘬๖ν A ∪B ⮳せk ๖ٲ㉏ȡ⪈㐈䄪㔴䃰ᬽȡ
ఏₓ喌ᝀЛञДᩭᓲ⮳ݏ䮓A ᪟㏳⮳䔈k/2 ͙ٲ㉏ȡऻ⤵喌ᒂA[k/2-1] > B[k/2-1] ᬥ喌ञ
Дݏ䮓B ᪟㏳⮳k/2 ͙ٲ㉏ȡ
ᒂA[k/2-1] == B[k/2-1] ᬥ喌䄣ᬽឭݟεせk ๖⮳ٲ㉏喌Ⱓᣔ䔃఍A[k/2-1] ᝅB[k/2-1]
ࢢञȡ
ఏₓ喌ᝀЛञДۈ̯͙䕁ᒁܬ᪟ȡ䗒ͷܬ᪟ϯͷᬥՈᏃ䄔㏷ₑ঑喟
• ᒂA ᝅB ᭞⾩ᬥ喌Ⱓᣔ䔃఍B[k-1] ᝅA[k-1]喛
• ᒂk=1 ᭞喌䔃఍min(A[0], B[0])喛
• ᒂA[k/2-1] == B[k/2-1] ᬥ喌䔃఍A[k/2-1] ᝅB[k/2-1]

---

8
せ2 』
㏮ᕖ㶗
Вⴰ
// LeetCode, Median of Two Sorted Arrays
// ᬥ䬣฼ᱱᏕO(log(m+n))喌⾩䬣฼ᱱᏕO(log(m+n))
class Solution {
public:
double findMedianSortedArrays(const vector<int>& A, const vector<int>& B) {
const int m = A.size();
const int n = B.size();
int total = m + n;
if (total & 0x1)
return find_kth(A.begin(), m, B.begin(), n, total / 2 + 1);
else
return (find_kth(A.begin(), m, B.begin(), n, total / 2)
+ find_kth(A.begin(), m, B.begin(), n, total / 2 + 1)) / 2.0;
}
private:
static int find_kth(std::vector<int>::const_iterator A, int m,
std::vector<int>::const_iterator B, int n, int k) {
//always assume that m is equal or smaller than n
if (m > n) return find_kth(B, n, A, m, k);
if (m == 0) return *(B + k - 1);
if (k == 1) return min(*A, *B);
//divide k into two parts
int ia = min(k / 2, m), ib = k - ia;
if (*(A + ia - 1) < *(B + ib - 1))
return find_kth(A + ia, m - ia, B, n, k - ia);
else if (*(A + ia - 1) > *(B + ib - 1))
return find_kth(A, m, B + ib, n - ib, k - ib);
else
return A[ia - 1];
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.6
Longest Consecutive Sequence
᣾䔟
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1,
2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.

---

2.1
᪟㏳
9
ܵᲿ
ັ᳋ٰ䃧O(n log n) ⮳฼ᱱᏕ喌䗒ͷञДٷᣁᎾ喌ञ᭞ᱛ题㺰ⅱO(n)ȡ
⩠νᎾ݆䛻⮳ٲ㉏᭞ᬏᎾ⮳喌ࣷ㺰ⅱO(n)喌仅ٷ㺰ᘢݟ⩗৷ጻ㶗ȡ
⩗̯͙৷ጻ㶗unordered_map<int, bool> used 䃟ᒄ⃾͙ٲ㉏᭞ॕҮ⩗喌ᄨ⃾͙ٲ㉏喌Д䄔ٲ
㉏ͩ͜ᓲ喌ᒯጕढមᑏ喌Ⱓݟ̼䔍㐜ͩₑ喌䃟ᒄ̺ᰯ䪮⮳䪮Ꮥȡ
Вⴰ
// Leet Code, Longest Consecutive Sequence
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int longestConsecutive(const vector<int> &nums) {
unordered_map<int, bool> used;
for (auto i : nums) used[i] = false;
int longest = 0;
for (auto i : nums) {
if (used[i]) continue;
int length = 1;
used[i] = true;
for (int j = i + 1; used.find(j) != used.end(); ++j) {
used[j] = true;
++length;
}
for (int j = i - 1; used.find(j) != used.end(); --j) {
used[j] = true;
++length;
}
longest = max(longest, length);
}
return longest;
}
};
ܵᲿ2
せ̯Ⱓ㻸᭞͙㖉ㆪ⮳᧼ҋ, Ꮓ䄔᰸union,find ⮳᧼ҋ. 䔍㐜Ꮎ݆ञД⩗͓〞঻䪮ᏕᲔ㶗
⹩.
ᱛᲔ⩗͓〞ᅠञД㶗⹩, ѵ㔲㮀ݟᴔ䄑⮳䰯ⅱ, ᄵ͓〞ܵݚᯣ䱡ܩᲔ. ⩗
unordered_-
map<int,
int> map Ეႇח. ࣎໺ᕌ䌞Ე㜙νhttp://discuss.leetcode.com/questions/1070/

---

10
せ2 』
㏮ᕖ㶗
longest-consecutive-sequence
Вⴰ
// Leet Code, Longest Consecutive Sequence
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
// Author: @advancedxy
class Solution {
public:
int longestConsecutive(vector<int> &nums) {
unordered_map<int, int> map;
int size = nums.size();
int l = 1;
for (int i = 0; i < size; i++) {
if (map.find(nums[i]) != map.end()) continue;
map[nums[i]] = 1;
if (map.find(nums[i] - 1) != map.end()) {
l = max(l, mergeCluster(map, nums[i] - 1, nums[i]));
}
if (map.find(nums[i] + 1) != map.end()) {
l = max(l, mergeCluster(map, nums[i], nums[i] + 1));
}
}
return size == 0 ? 0 : l;
}
private:
int mergeCluster(unordered_map<int, int> &map, int left, int right) {
int upper = right + map[right] - 1;
int lower = left - map[left] + 1;
int length = upper - lower + 1;
map[upper] = length;
map[lower] = length;
return length;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.7
Two Sum
᣾䔟
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where
index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not
zero-based.

---

2.1
᪟㏳
11
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
ܵᲿ
᫨∄1喚ᯣߊ喌฼ᱱᏕO(n2)喌щ䊴ᬥ
᫨∄2喚hashȡ⩗̯͙৷ጻ㶗喌ႇח⃾͙᪟ᄨᏃ⮳̺ᴶ喌฼ᱱᏕO(n).
᫨∄3喚ٷᣁᎾ喌♥ऽጕढ๨䕫喌ᣁᎾO(n log n)喌ጕढ๨䕫O(n)喌ᰯ㏷O(n log n)ȡѵ᭞∗ᘾ喌
䔈题䰯㺰䔃఍⮳᭞̺ᴶ喌㔻̼᭞᪟ႆᱛ䏚喌ఏₓ䔈͙᫨∄㵻̼䕉ȡ
Вⴰ
//LeetCode, Two Sum
// ᫨∄2喚hashȡ⩗̯͙৷ጻ㶗喌ႇח⃾͙᪟ᄨᏃ⮳̺ᴶ
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<int> twoSum(vector<int> &nums, int target) {
unordered_map<int, int> mapping;
vector<int> result;
for (int i = 0; i < nums.size(); i++) {
mapping[nums[i]] = i;
}
for (int i = 0; i < nums.size(); i++) {
const int gap = target - nums[i];
if (mapping.find(gap) != mapping.end() && mapping[gap] > i) {
result.push_back(i + 1);
result.push_back(mapping[gap] + 1);
break;
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• 3Sum, 㻰§2.1.8
• 3Sum Closest, 㻰§2.1.9
• 4Sum, 㻰§2.1.10

---

12
せ2 』
㏮ᕖ㶗
2.1.8
3Sum
᣾䔟
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique
triplets in the array which gives the sum of zero.
Note:
• Elements in a triplet (a, b, c) must be in non-descending order. (ie, a ≤b ≤c)
• The solution set must not contain duplicate triplets.
For example, given array S = {-1 0 1 2 -1 -4}.
A solution set is:
(-1, 0, 1)
(-1, -1, 2)
ܵᲿ
ٷᣁᎾ喌♥ऽጕढ๨䕫喌฼ᱱᏕO(n2)ȡ
䔈͙᫨∄ञДᣗᎮݟk-sum喌ٷᣁᎾ喌♥ऽ։ k −2 ⁐ᓙ⣞喌౗ᰯڴᅱᓙ⣞ጕढ๨䕫喌ᬥ䬣฼ᱱ
Ꮥ᭞O(max{n log n, nk−1})ȡ
Вⴰ
// LeetCode, 3Sum
// ٷᣁᎾ喌♥ऽጕढ๨䕫喌∗ᘾ䌢䓶䛼฼⮳᪟喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int>> threeSum(vector<int>& nums) {
vector<vector<int>> result;
if (nums.size() < 3) return result;
sort(nums.begin(), nums.end());
const int target = 0;
auto last = nums.end();
for (auto i = nums.begin(); i < last-2; ++i) {
auto j = i+1;
if (i > nums.begin() && *i == *(i-1)) continue;
auto k = last-1;
while (j < k) {
if (*i + *j + *k < target) {
++j;
while(*j == *(j - 1) && j < k) ++j;
} else if (*i + *j + *k > target) {
--k;
while(*k == *(k + 1) && j < k) --k;
} else {
result.push_back({ *i, *j, *k });
++j;

---

2.1
᪟㏳
13
--k;
while(*j == *(j - 1) && *k == *(k + 1) && j < k) ++j;
}
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• Two sum, 㻰§2.1.7
• 3Sum Closest, 㻰§2.1.9
• 4Sum, 㻰§2.1.10
2.1.9
3Sum Closest
᣾䔟
Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
ܵᲿ
ٷᣁᎾ喌♥ऽጕढ๨䕫喌฼ᱱᏕO(n2)ȡ
Вⴰ
// LeetCode, 3Sum Closest
// ٷᣁᎾ喌♥ऽጕढ๨䕫喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int threeSumClosest(vector<int>& nums, int target) {
int result = 0;
int min_gap = INT_MAX;
sort(nums.begin(), nums.end());
for (auto a = nums.begin(); a != prev(nums.end(), 2); ++a) {
auto b = next(a);
auto c = prev(nums.end());
while (b < c) {
const int sum = *a + *b + *c;
const int gap = abs(sum - target);

---

14
せ2 』
㏮ᕖ㶗
if (gap < min_gap) {
result = sum;
min_gap = gap;
}
if (sum < target) ++b;
else
--c;
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• Two sum, 㻰§2.1.7
• 3Sum, 㻰§2.1.8
• 4Sum, 㻰§2.1.10
2.1.10
4Sum
᣾䔟
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
Note:
• Elements in a quadruplet (a, b, c, d) must be in non-descending order. (ie, a ≤b ≤c ≤d)
• The solution set must not contain duplicate quadruplets.
For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
A solution set is:
(-1,
0, 0, 1)
(-2, -1, 1, 2)
(-2,
0, 0, 2)
ܵᲿ
ٷᣁᎾ喌♥ऽጕढ๨䕫喌฼ᱱᏕO(n3)喌щ䊴ᬥȡ
ञД⩗̯͙ hashmap ٷ㑂ႇ͓͙᪟⮳঻喌ᰯ㏷฼ᱱᏕO(n3)ȡ䔈͙ゅ⪔Ύ䔱⩗ν 3Sum ȡ

---

2.1
᪟㏳
15
ጕढ๨䕫
// LeetCode, 4Sum
// ٷᣁᎾ喌♥ऽጕढ๨䕫喌ᬥ䬣฼ᱱᏕO(n^3)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int>> fourSum(vector<int>& nums, int target) {
vector<vector<int>> result;
if (nums.size() < 4) return result;
sort(nums.begin(), nums.end());
auto last = nums.end();
for (auto a = nums.begin(); a < prev(last, 3); ++a) {
for (auto b = next(a); b < prev(last, 2); ++b) {
auto c = next(b);
auto d = prev(last);
while (c < d) {
if (*a + *b + *c + *d < target) {
++c;
} else if (*a + *b + *c + *d > target) {
--d;
} else {
result.push_back({ *a, *b, *c, *d });
++c;
--d;
}
}
}
}
sort(result.begin(), result.end());
result.erase(unique(result.begin(), result.end()), result.end());
return result;
}
};
map ։㑂ႇ
// LeetCode, 4Sum
// ⩗̯͙ hashmap ٷ㑂ႇ͓͙᪟⮳঻
// ᬥ䬣฼ᱱᏕ喌Ꭲ౶O(n^2)喌ᰯ౾O(n^4)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
vector<vector<int> > fourSum(vector<int> &nums, int target) {
vector<vector<int>> result;
if (nums.size() < 4) return result;
sort(nums.begin(), nums.end());
unordered_map<int, vector<pair<int, int> > > cache;
for (size_t a = 0; a < nums.size(); ++a) {
for (size_t b = a + 1; b < nums.size(); ++b) {
cache[nums[a] + nums[b]].push_back(pair<int, int>(a, b));
}
}

---

16
せ2 』
㏮ᕖ㶗
for (int c = 0; c < nums.size(); ++c) {
for (size_t d = c + 1; d < nums.size(); ++d) {
const int key = target - nums[c] - nums[d];
if (cache.find(key) == cache.end()) continue;
const auto& vec = cache[key];
for (size_t k = 0; k < vec.size(); ++k) {
if (c <= vec[k].second)
continue; // ᰸䛼ए
result.push_back( { nums[vec[k].first],
nums[vec[k].second], nums[c], nums[d] });
}
}
}
sort(result.begin(), result.end());
result.erase(unique(result.begin(), result.end()), result.end());
return result;
}
};
multimap
// LeetCode, 4Sum
// ⩗̯͙ hashmap ٷ㑂ႇ͓͙᪟⮳঻
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
// @author 哉䭵Ⴘ(http://weibo.com/luangong)
class Solution {
public:
vector<vector<int>> fourSum(vector<int>& nums, int target) {
vector<vector<int>> result;
if (nums.size() < 4) return result;
sort(nums.begin(), nums.end());
unordered_multimap<int, pair<int, int>> cache;
for (int i = 0; i + 1 < nums.size(); ++i)
for (int j = i + 1; j < nums.size(); ++j)
cache.insert(make_pair(nums[i] + nums[j], make_pair(i, j)));
for (auto i = cache.begin(); i != cache.end(); ++i) {
int x = target - i->first;
auto range = cache.equal_range(x);
for (auto j = range.first; j != range.second; ++j) {
auto a = i->second.first;
auto b = i->second.second;
auto c = j->second.first;
auto d = j->second.second;
if (a != c && a != d && b != c && b != d) {
vector<int> vec = { nums[a], nums[b], nums[c], nums[d] };
sort(vec.begin(), vec.end());
result.push_back(vec);
}

---

2.1
᪟㏳
17
}
}
sort(result.begin(), result.end());
result.erase(unique(result.begin(), result.end()), result.end());
return result;
}
};
᫨∄4
// LeetCode, 4Sum
// ٷᣁᎾ喌♥ऽጕढ๨䕫喌ᬥ䬣฼ᱱᏕO(n^3logn)喌⾩䬣฼ᱱᏕO(1)喌щ䊴ᬥ
// 䌎᫨∄1 Ⱗ℃喌㶗䲑̹чࡅε喌Ⴭ䭴̹ᰣᚑε喌ܶ䃟喁
class Solution {
public:
vector<vector<int>> fourSum(vector<int>& nums, int target) {
vector<vector<int>> result;
if (nums.size() < 4) return result;
sort(nums.begin(), nums.end());
auto last = nums.end();
for (auto a = nums.begin(); a < prev(last, 3);
a = upper_bound(a, prev(last, 3), *a)) {
for (auto b = next(a); b < prev(last, 2);
b = upper_bound(b, prev(last, 2), *b)) {
auto c = next(b);
auto d = prev(last);
while (c < d) {
if (*a + *b + *c + *d < target) {
c = upper_bound(c, d, *c);
} else if (*a + *b + *c + *d > target) {
d = prev(lower_bound(c, d, *d));
} else {
result.push_back({ *a, *b, *c, *d });
c = upper_bound(c, d, *c);
d = prev(lower_bound(c, d, *d));
}
}
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• Two sum, 㻰§2.1.7
• 3Sum, 㻰§2.1.8
• 3Sum Closest, 㻰§2.1.9

---

18
せ2 』
㏮ᕖ㶗
2.1.11
Remove Element
᣾䔟
Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn’t matter what you leave beyond the new length.
ܵᲿ
ᬏ
Вⴰ1
// LeetCode, Remove Element
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int removeElement(vector<int>& nums, int target) {
int index = 0;
for (int i = 0; i < nums.size(); ++i) {
if (nums[i] != target) {
nums[index++] = nums[i];
}
}
return index;
}
};
Вⴰ2
// LeetCode, Remove Element
// Ү⩗remove()喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int removeElement(vector<int>& nums, int target) {
return distance(nums.begin(), remove(nums.begin(), nums.end(), target));
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

2.1
᪟㏳
19
2.1.12
Next Permutation
᣾䔟
Implement next permutation, which rearranges numbers into the lexicographically next greater permu-
tation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascend-
ing order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the
right-hand column.
1,2,3 →1,3,2
3,2,1 →1,2,3
1,1,5 →1,5,1
ܵᲿ
テ∄䓶⼺ັభ2-1ᝯ⹩喈Ე㜙http://ﬁsherlei.blogspot.com/2012/12/leetcode-next-permutation.html喉ȡ
భ2-1
̺̯͙ᣁ݆テ∄≰⼺

![Leetcode-CPP 第25页插图](../assets/images/Leetcode-CPP_p25_1_05693ea3.png)

---

20
せ2 』
㏮ᕖ㶗
Вⴰ
// LeetCode, Next Permutation
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void nextPermutation(vector<int> &nums) {
next_permutation(nums.begin(), nums.end());
}
template<typename BidiIt>
bool next_permutation(BidiIt first, BidiIt last) {
// Get a reversed range to simplify reversed traversal.
const auto rfirst = reverse_iterator<BidiIt>(last);
const auto rlast = reverse_iterator<BidiIt>(first);
// Begin from the second last element to the first element.
auto pivot = next(rfirst);
// Find `pivot`, which is the first element that is no less than its
// successor.
`Prev` is used since `pivort` is a `reversed_iterator`.
while (pivot != rlast && *pivot >= *prev(pivot))
++pivot;
// No such elemenet found, current sequence is already the largest
// permutation, then rearrange to the first permutation and return false.
if (pivot == rlast) {
reverse(rfirst, rlast);
return false;
}
// Scan from right to left, find the first element that is greater than
// `pivot`.
auto change = find_if(rfirst, pivot, bind1st(less<int>(), *pivot));
swap(*change, *pivot);
reverse(rfirst, pivot);
return true;
}
};
Ⱗڢ题Ⱍ
• Permutation Sequence, 㻰§2.1.13
• Permutations, 㻰§8.3
• Permutations II, 㻰§8.4
• Combinations, 㻰§8.5

---

2.1
᪟㏳
21
2.1.13
Permutation Sequence
᣾䔟
The set [1,2,3,ĉ,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.
ܵᲿ
クࢄ⮳喌ञД⩗ᯣߊ᳉ͭ∄喌䄲⩗k −1 ⁐ next_permutation()ȡ
ᯣߊ᳉ͭ∄ឹݼk ͙ᣁ݆䘬ⅱܩᲔε喌℃䒲⊙䉨喌㔻ᝀЛङ䰯㺰せk ͙ᣁ݆ȡ
ݘ⩗Ꮶជ㑅ⴰ⮳ᕌ䌞喌ն䃭᰸n ͙̼䛼฼⮳ٲ㉏喌せk ͙ᣁ݆᭞a1, a2, a3, ..., an喌䗒ͷ a1 ᭞ਙ
̯͙Ѽ㒝঑喟
ᝀЛឹa1 ࣪ᢸ喌䗒ͷޘ̺⮳ᣁ݆ͩ a2, a3, ..., an, ڠ䃐n −1 ͙ٲ㉏喌n −1 ͙ٲ㉏ڠ᰸(n −1)!
͙ᣁ݆喌ν᭞ᅠञДⴔ䖂a1 = k/(n −1)!ȡ
ऻ⤵喌a2, a3, ..., an ⮳իᣗᄫັ̺喚
k2
=
k%(n −1)!
a2
=
k2/(n −2)!
· · ·
kn−1
=
kn−2%2!
an−1
=
kn−1/1!
an
=
0
Ү⩗next_permutation()
// LeetCode, Permutation Sequence
// Ү⩗next_permutation()喌TLE
class Solution {
public:
string getPermutation(int n, int k) {
string s(n, '0');
for (int i = 0; i < n; ++i)

---

22
せ2 』
㏮ᕖ㶗
s[i] += i+1;
for (int i = 0; i < k-1; ++i)
next_permutation(s.begin(), s.end());
return s;
}
template<typename BidiIt>
bool next_permutation(BidiIt first, BidiIt last) {
// Вⴰ㻰̹̯题Next Permutation
}
};
Ꮶជ㑅ⴰ
// LeetCode, Permutation Sequence
// Ꮶជ㑅ⴰ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
string getPermutation(int n, int k) {
string s(n, '0');
string result;
for (int i = 0; i < n; ++i)
s[i] += i + 1;
return kth_permutation(s, k);
}
private:
int factorial(int n) {
int result = 1;
for (int i = 1; i <= n; ++i)
result *= i;
return result;
}
// seq ጡᣁຬᎾ喌᭞せ̯͙ᣁ݆
template<typename Sequence>
Sequence kth_permutation(const Sequence &seq, int k) {
const int n = seq.size();
Sequence S(seq);
Sequence result;
int base = factorial(n - 1);
--k;
// Ꮶជ㑅ⴰϽ 0 ᐯ໺
for (int i = n - 1; i > 0; k %= base, base /= i, --i) {
auto a = next(S.begin(), k / base);
result.push_back(*a);
S.erase(a);
}
result.push_back(S[0]); // ᰯऽ̯͙
return result;
}

---

2.1
᪟㏳
23
};
Ⱗڢ题Ⱍ
• Next Permutation, 㻰§2.1.12
• Permutations, 㻰§8.3
• Permutations II, 㻰§8.4
• Combinations, 㻰§8.5
2.1.14
Valid Sudoku
᣾䔟
Determine
if
a
Sudoku
is
valid,
according
to:
Sudoku
Puzzles
-
The
Rules
http://sudoku.com.au/TheRules.aspx .
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
భ2-2
A partially filled sudoku which is valid
ܵᲿ
㏵㞱Ⴭ⣟题ȡ
Вⴰ
// LeetCode, Valid Sudoku
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool isValidSudoku(const vector<vector<char>>& board) {
bool used[9];

![Leetcode-CPP 第29页插图](../assets/images/Leetcode-CPP_p29_1_6edaa7d2.png)

---

24
せ2 』
㏮ᕖ㶗
for (int i = 0; i < 9; ++i) {
fill(used, used + 9, false);
for (int j = 0; j < 9; ++j) // ᷯᴔ㵻
if (!check(board[i][j], used))
return false;
fill(used, used + 9, false);
for (int j = 0; j < 9; ++j) // ᷯᴔ݆
if (!check(board[j][i], used))
return false;
}
for (int r = 0; r < 3; ++r) // ᷯᴔ9 ͙ၿᵫၿ
for (int c = 0; c < 3; ++c) {
fill(used, used + 9, false);
for (int i = r * 3; i < r * 3 + 3; ++i)
for (int j = c * 3; j < c * 3 + 3; ++j)
if (!check(board[i][j], used))
return false;
}
return true;
}
bool check(char ch, bool used[9]) {
if (ch == '.') return true;
if (used[ch - '1']) return false;
return used[ch - '1'] = true;
}
};
Ⱗڢ题Ⱍ
• Sudoku Solver, 㻰§10.10
2.1.15
Trapping Rain Water
᣾䔟
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute
how much water it is able to trap after raining.
For example, Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

---

2.1
᪟㏳
25
భ2-3
Trapping Rain Water
ܵᲿ
ᄨν⃾͙ᴠၿ喌ឭݟڥጕढ͓䓨ᰯ倇⮳ᴠၿ喌䄔ᴠၿ㘬შ㏢⮳䲑⼞ᅠ᭞min(max_left, max_-
right) - heightȡᝯД喌
1. Ͻጕᒯढរ᣾̯䕼喌ᄨν⃾͙ᴠၿ喌ⅱअጕ䓨ᰯ๖ի喛
2. Ͻढᒯጕរ᣾̯䕼喌ᄨν⃾͙ᴠၿ喌ⅱᰯ๖ढի喛
3. ڼរ᣾̯䕼喌ឹ⃾͙ᴠၿ⮳䲑⼞Ꭵ㉞ߏȡ
ΎञД喌
1. រ᣾̯䕼喌ឭݟᰯ倇⮳ᴠၿ喌䔈͙ᴠၿᄵ᪟㏳͓ܵͩࡹ喛
2. ำ⤵ጕ䓨̯ࡹ喛
3. ำ⤵ढ䓨̯ࡹȡ
Вⴰ1
// LeetCode, Trapping Rain Water
// ᕌ䌞1喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int trap(const vector<int>& A) {
const int n = A.size();
int *max_left = new int[n]();
int *max_right = new int[n]();
for (int i = 1; i < n; i++) {
max_left[i] = max(max_left[i - 1], A[i - 1]);
max_right[n - 1 - i] = max(max_right[n - i], A[n - i]);
}
int sum = 0;
for (int i = 0; i < n; i++) {

![Leetcode-CPP 第31页插图](../assets/images/Leetcode-CPP_p31_1_7a1bc105.png)

---

26
せ2 』
㏮ᕖ㶗
int height = min(max_left[i], max_right[i]);
if (height > A[i]) {
sum += height - A[i];
}
}
delete[] max_left;
delete[] max_right;
return sum;
}
};
Вⴰ2
// LeetCode, Trapping Rain Water
// ᕌ䌞2喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int trap(const vector<int>& A) {
const int n = A.size();
int max = 0; // ᰯ倇⮳ᴠၿ喌ᄵ᪟㏳͓ܵͩࡹ
for (int i = 0; i < n; i++)
if (A[i] > A[max]) max = i;
int water = 0;
for (int i = 0, peak = 0; i < max; i++)
if (A[i] > peak) peak = A[i];
else water += peak - A[i];
for (int i = n - 1, top = 0; i > max; i--)
if (A[i] > top) top = A[i];
else water += top - A[i];
return water;
}
};
Вⴰ3
せ̸⻼解∄喌⩗̯͙ᴷ䒴ߘ喌ᄾνᴷ䶥⮳ٲ㉏ࢺڔ喌๖νへνᴷ䶥ᅠឹᴷ䛻ᝯ᰸ᄾνᝅへνᒂ
ݼի⮳ٲ㉏ڗ䘗ܩᴷำ⤵ᢸȡ
// LeetCode, Trapping Rain Water
// ⩗̯͙ᴷ䒴ߘ喌ᄾνᴷ䶥⮳ٲ㉏ࢺڔ喌๖νへνᴷ䶥ᅠឹᴷ䛻ᝯ᰸ᄾνᝅ
// へνᒂݼի⮳ٲ㉏ڗ䘗ܩᴷำ⤵ᢸ喌䃐テ䲑⼞喌ᰯऽឹᒂݼٲ㉏ڔᴷ
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int trap(const vector<int>& A) {
const int n = A.size();
stack<pair<int, int>> s;
int water = 0;
for (int i = 0; i < n; ++i) {

---

2.1
᪟㏳
27
int height = 0;
while (!s.empty()) { // ᄵᴷ䛻℃ᒂݼٲ㉏ⴝᝅへ倇⮳ٲ㉏ڗ䘗ำ⤵ᢸ
int bar = s.top().first;
int pos = s.top().second;
// bar, height, A[i] ̸㔴๨᜿⮳ܨ䮦
water += (min(bar, A[i]) - height) * (i - pos - 1);
height = bar;
if (A[i] < bar) // ⷟ݟε℃ᒂݼٲ㉏倇⮳喌䌢ܩᓙ⣞
break;
else
s.pop(); // ᑨܩᴷ䶥喌ఏͩ䄔ٲ㉏ำ⤵Ⴛε喌̼ڼ䰯㺰ε
}
s.push(make_pair(A[i], i));
}
return water;
}
};
Ⱗڢ题Ⱍ
• Container With Most Water, 㻰§12.6
• Largest Rectangle in Histogram, 㻰§4.1.3
2.1.16
Rotate Image
᣾䔟
You are given an n × n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up: Could you do this in-place?
ܵᲿ
仅ٷᘢݟ喌㏞ὐ᠎喌Ͻๅݟڴ̯ష̯ష⮳䒛喌ѵ䔈͙᫨∄๙ᚑȡ
ັ̺భ喌仅ٷ⇮Ɐޞᄨ㼁㏮㔪䒛̯⁐喌♥ऽ⇮ⱯⅣᎢ͜㏮㔪䒛̯⁐ȡ
భ2-4
Rotate Image
ᝅ㔴喌仅ٷ⇮ⱯⅣᎢ͜㏮㔪䒛̯⁐喌♥ऽ⇮Ɐͪᄨ㼁㏮㔪䒛̯⁐ȡ

![Leetcode-CPP 第33页插图](../assets/images/Leetcode-CPP_p33_1_e8250528.png)

---

28
せ2 』
㏮ᕖ㶗
Вⴰ1
// LeetCode, Rotate Image
// ᕌ䌞1喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void rotate(vector<vector<int>>& matrix) {
const int n = matrix.size();
for (int i = 0; i < n; ++i)
// ⇮Ɐޞᄨ㼁㏮ࣼ䒛
for (int j = 0; j < n - i; ++j)
swap(matrix[i][j], matrix[n - 1 - j][n - 1 - i]);
for (int i = 0; i < n / 2; ++i) // ⇮ⱯⅣᎢ͜㏮ࣼ䒛
for (int j = 0; j < n; ++j)
swap(matrix[i][j], matrix[n - 1 - i][j]);
}
};
Вⴰ2
// LeetCode, Rotate Image
// ᕌ䌞2喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void rotate(vector<vector<int>>& matrix) {
const int n = matrix.size();
for (int i = 0; i < n / 2; ++i) // ⇮ⱯⅣᎢ͜㏮ࣼ䒛
for (int j = 0; j < n; ++j)
swap(matrix[i][j], matrix[n - 1 - i][j]);
for (int i = 0; i < n; ++i)
// ⇮Ɐͪᄨ㼁㏮ࣼ䒛
for (int j = i + 1; j < n; ++j)
swap(matrix[i][j], matrix[j][i]);
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.17
Plus One
᣾䔟
Given a number represented as an array of digits, plus one to the number.

---

2.1
᪟㏳
29
ܵᲿ
倇㇭Ꮥߏ∄ȡ
Вⴰ1
// LeetCode, Plus One
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> plusOne(vector<int> &digits) {
add(digits, 1);
return digits;
}
private:
// 0 <= digit <= 9
void add(vector<int> &digits, int digit) {
int c = digit;
// carry, 䔊Ѽ
for (auto it = digits.rbegin(); it != digits.rend(); ++it) {
*it += c;
c = *it / 10;
*it %= 10;
}
if (c > 0) digits.insert(digits.begin(), 1);
}
};
Вⴰ2
// LeetCode, Plus One
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> plusOne(vector<int> &digits) {
add(digits, 1);
return digits;
}
private:
// 0 <= digit <= 9
void add(vector<int> &digits, int digit) {
int c = digit;
// carry, 䔊Ѽ
for_each(digits.rbegin(), digits.rend(), [&c](int &d){
d += c;
c = d / 10;
d %= 10;
});
if (c > 0) digits.insert(digits.begin(), 1);

---

30
せ2 』
㏮ᕖ㶗
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.18
Climbing Stairs
᣾䔟
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
ܵᲿ
䃭f(n) 㶗⹩❛n 䭥ẫᷞ⮳̼ऻ᫨∄᪟喌ͩε❛ݟせn 䭥ẫᷞ喌᰸͓͙䔸᠘喚
• Ͻせn −1 䭥ݼ䔊1 ₔ喛
• Ͻせn −1 䭥ݼ䔊2 ₔ喛
ఏₓ喌᰸f(n) = f(n −1) + f(n −2)ȡ
䔈᭞̯͙ᪿ∑䗒຀᪟݆ȡ
᫨∄1喌䕁ᒁ喌๙ᚑ喛᫨∄2喌䔜Вȡ
᫨∄3喌᪟႕ڛᐾȡᪿ∑䗒຀᪟݆⮳䕉䶨ڛᐾͩ an =
1
√
5
[(1 +
√
5
2
)n
−
(1 −
√
5
2
)n]
ȡ
䔜В
// LeetCode, Climbing Stairs
// 䔜В喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int climbStairs(int n) {
int prev = 0;
int cur = 1;
for(int i = 1; i <= n ; ++i){
int tmp = cur;
cur += prev;
prev = tmp;
}
return cur;
}
};

---

2.1
᪟㏳
31
᪟႕ڛᐾ
// LeetCode, Climbing Stairs
// ᪟႕ڛᐾ喌ᬥ䬣฼ᱱᏕO(1)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int climbStairs(int n) {
const double s = sqrt(5);
return floor((pow((1+s)/2, n+1) + pow((1-s)/2, n+1))/s + 0.5);
}
};
Ⱗڢ题Ⱍ
• Decode Ways, 㻰§13.10
2.1.19
Gray Code
᣾䔟
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of
gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
Note:
• For a given n, a gray code sequence is not uniquely defined.
• For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
• For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
ܵᲿ
ᵫ䰦ⴰ(Gray Code) ⮳჉͸䄦ࣱ㔲http://en.wikipedia.org/wiki/Gray_code
㜙♥λ䔊ݥⴰ䒛ᢑͩᵫ䰦ⴰ喚g0 = b0, gi = bi ⊕bi−1
Ԍ⪈㜙♥λ䔊ݥⴰ⮳ᰯ倇Ѽҋͩᵫ䰦ⴰ⮳ᰯ倇Ѽ喌ᵫ䰦ⴰ⁐倇Ѽͩλ䔊ݥⴰ⮳倇Ѽ̽⁐倇Ѽᐱ
ᝅ喌ڥ҈ळѼ̽⁐倇Ѽ⮳ⅱ∄ㆪѫȡҺັ喌ᄵ㜙♥λ䔊ݥⴰ1001喌䒛ᢑͩᵫ䰦ⴰ⮳䓶⼺᭞喚Ԍ⪈ᰯ
倇Ѽ喛♥ऽᄵせ1 Ѽ⮳1 ঻せ2 Ѽ⮳0 ᐱᝅ喌ᓆݟ1喌ҋͩᵫ䰦ⴰ⮳せ2 Ѽ喛ᄵせ2 Ѽ⮳0 ঻せ3 Ѽ
⮳0 ᐱᝅ喌ᓆݟ0喌ҋͩᵫ䰦ⴰ⮳せ3 Ѽ喛ᄵせ3 Ѽ⮳0 ঻せ4 Ѽ⮳1 ᐱᝅ喌ᓆݟ1喌ҋͩᵫ䰦ⴰ⮳
せ4 Ѽ喌ᰯ㏷喌ᵫ䰦ⴰͩ 1101ȡ
ᵫ䰦ⴰ䒛ᢑͩ㜙♥λ䔊ݥⴰ喚b0 = g0, bi = gi ⊕bi−1

---

32
せ2 』
㏮ᕖ㶗
Ԍ⪈ᵫ䰦ⴰ⮳ᰯ倇Ѽҋͩ㜙♥λ䔊ݥⴰ⮳ᰯ倇Ѽ喌⁐倇Ѽͩ㜙♥λ䔊ݥ倇Ѽ̽ᵫ䰦ⴰ⁐倇Ѽᐱ
ᝅ喌ڥ҈ळѼ̽⁐倇Ѽ⮳ⅱ∄ㆪѫȡҺັ喌ᄵᵫ䰦ⴰ1000 䒛ᢑͩ㜙♥λ䔊ݥⴰ⮳䓶⼺᭞喚Ԍ⪈ᰯ倇
Ѽ 1喌ҋͩ㜙♥λ䔊ݥⴰ⮳ᰯ倇Ѽ喛♥ऽᄵ㜙♥λ䔊ݥⴰ⮳せ1 Ѽ 1 ঻ᵫ䰦ⴰ⮳せ2 Ѽ 0 ᐱᝅ喌ᓆݟ
1喌ҋͩ㜙♥λ䔊ݥⴰ⮳せ2 Ѽ喛ᄵ㜙♥λ䔊ݥⴰ⮳せ2 Ѽ 1 ঻ᵫ䰦ⴰ⮳せ3 Ѽ 0 ᐱᝅ喌ᓆݟ1喌ҋ
ͩ㜙♥λ䔊ݥⴰ⮳せ3 Ѽ喛ᄵ㜙♥λ䔊ݥⴰ⮳せ3 Ѽ 1 ঻ᵫ䰦ⴰ⮳せ4 Ѽ 0 ᐱᝅ喌ᓆݟ1喌ҋͩ㜙♥
λ䔊ݥⴰ⮳せ4 Ѽ喌ᰯ㏷喌㜙♥λ䔊ݥⴰͩ 1111ȡ
ᵫ䰦ⴰ᰸᪟႕ڛᐾ喌᪣᪟n ⮳ᵫ䰦ⴰ᭞n ⊕(n/2)ȡ
䔈题㺰ⅱ⩎᜿n ℃➨⮳ᝯ᰸ᵫ䰦ⴰȡ
᫨∄1喌ᰯクࢄ⮳᫨∄喌ݘ⩗᪟႕ڛᐾ喌ᄨϽ 0 ∼2n −1 ⮳ᝯ᰸᪣᪟喌䒛ࡅͩᵫ䰦ⴰȡ
᫨∄2喌n ℃➨⮳ᵫ䰦ⴰ喌ञД䕁ᒁ౟Ͻ n −1 ℃➨⮳ᵫ䰦ⴰ⩎᜿ȡັభ§2-5ᝯ⹩ȡ
భ2-5
The first few steps of the reflect-and-prefix method.
᪟႕ڛᐾ
// LeetCode, Gray Code
// ᪟႕ڛᐾ喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> grayCode(int n) {
vector<int> result;
const size_t size = 1 << n;
// 2^n
result.reserve(size);
for (size_t i = 0; i < size; ++i)
result.push_back(binary_to_gray(i));
return result;
}
private:
static unsigned int binary_to_gray(unsigned int n) {
return n ^ (n >> 1);
}
};

![Leetcode-CPP 第38页插图](../assets/images/Leetcode-CPP_p38_1_f0098d9f.png)

---

2.1
᪟㏳
33
Reflect-and-prefix method
// LeetCode, Gray Code
// reflect-and-prefix method
// ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> grayCode(int n) {
vector<int> result;
result.reserve(1<<n);
result.push_back(0);
for (int i = 0; i < n; i++) {
const int highest_bit = 1 << i;
for (int j = result.size() - 1; j >= 0; j--) // 㺰ࣼⱯ䕼ࢵ喌᝼㘬ᄨ⼟
result.push_back(highest_bit | result[j]);
}
return result;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.20
Set Matrix Zeroes
᣾䔟
Given a m × n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Follow up: Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
ܵᲿ
O(m + n) ⾩䬣⮳᫨∄ᒷクࢄ喌䃭㒝͓͙ bool ᪟㏳喌䃟ᒄ⃾㵻঻⃾݆᭞ॕႇ౗0ȡ
ᘢ㺰፧᪟⾩䬣喌ञД฼⩗せ̯㵻঻せ̯݆ȡ
Вⴰ1
// LeetCode, Set Matrix Zeroes
// ᬥ䬣฼ᱱᏕO(m*n)喌⾩䬣฼ᱱᏕO(m+n)
class Solution {
public:
void setZeroes(vector<vector<int> > &matrix) {
const size_t m = matrix.size();
const size_t n = matrix[0].size();

---

34
せ2 』
㏮ᕖ㶗
vector<bool> row(m, false); // ᴶ䃟䄔㵻᭞ॕႇ౗0
vector<bool> col(n, false); // ᴶ䃟䄔݆᭞ॕႇ౗0
for (size_t i = 0; i < m; ++i) {
for (size_t j = 0; j < n; ++j) {
if (matrix[i][j] == 0) {
row[i] = col[j] = true;
}
}
}
for (size_t i = 0; i < m; ++i) {
if (row[i])
fill(&matrix[i][0], &matrix[i][0] + n, 0);
}
for (size_t j = 0; j < n; ++j) {
if (col[j]) {
for (size_t i = 0; i < m; ++i) {
matrix[i][j] = 0;
}
}
}
}
};
Вⴰ2
// LeetCode, Set Matrix Zeroes
// ᬥ䬣฼ᱱᏕO(m*n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void setZeroes(vector<vector<int> > &matrix) {
const size_t m = matrix.size();
const size_t n = matrix[0].size();
bool row_has_zero = false; // せ̯㵻᭞ॕႇ౗0
bool col_has_zero = false; // せ̯݆᭞ॕႇ౗0
for (size_t i = 0; i < n; i++)
if (matrix[0][i] == 0) {
row_has_zero = true;
break;
}
for (size_t i = 0; i < m; i++)
if (matrix[i][0] == 0) {
col_has_zero = true;
break;
}
for (size_t i = 1; i < m; i++)
for (size_t j = 1; j < n; j++)
if (matrix[i][j] == 0) {
matrix[0][j] = 0;

---

2.1
᪟㏳
35
matrix[i][0] = 0;
}
for (size_t i = 1; i < m; i++)
for (size_t j = 1; j < n; j++)
if (matrix[i][0] == 0 || matrix[0][j] == 0)
matrix[i][j] = 0;
if (row_has_zero)
for (size_t i = 0; i < n; i++)
matrix[0][i] = 0;
if (col_has_zero)
for (size_t i = 0; i < m; i++)
matrix[i][0] = 0;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.21
Gas Station
᣾䔟
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next
station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station’s index if you can travel around the circuit once, otherwise return -1.
Note: The solution is guaranteed to be unique.
ܵᲿ
仅ٷᘢݟ⮳᭞O(N 2) ⮳解∄喌ᄨ⃾͙◨䔊㵻ὐ᠎ȡ
O(N) ⮳解∄᭞喌䃭㒝͓͙इ䛾喌sum ݓ᫜ᒂݼ⮳ᠶ䦷⮳᰸᩷ᕖ喛total ݈ݓ᫜᪣͙᪟㏳᭞ॕ᰸
解喌᰸ᅠ䔃఍䕉䓶sum ᓆݟ⮳̺ᴶ喌⇐᰸݈䔃఍-1ȡ
Вⴰ
// LeetCode, Gas Station
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
int total = 0;
int j = -1;
for (int i = 0, sum = 0; i < gas.size(); ++i) {
sum += gas[i] - cost[i];
total += gas[i] - cost[i];

---

36
せ2 』
㏮ᕖ㶗
if (sum < 0) {
j = i;
sum = 0;
}
}
return total >= 0 ? j + 1 : -1;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.22
Candy
᣾䔟
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
• Each child must have at least one candy.
• Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
ܵᲿ
ᬏ
䔜В❷
// LeetCode, Candy
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int candy(vector<int> &ratings) {
const int n = ratings.size();
vector<int> increment(n);
// ጕढळរ᣾̯䕼
for (int i = 1, inc = 1; i < n; i++) {
if (ratings[i] > ratings[i - 1])
increment[i] = max(inc++, increment[i]);
else
inc = 1;
}
for (int i = n - 2, inc = 1; i >= 0; i--) {
if (ratings[i] > ratings[i + 1])

---

2.1
᪟㏳
37
increment[i] = max(inc++, increment[i]);
else
inc = 1;
}
// ݌໺իͩ n喌ఏͩ⃾͙ᄾ᰺ࣺ㜢ᅀ̯䷆㈅
return accumulate(&increment[0], &increment[0]+n, n);
}
};
䕁ᒁ❷
// LeetCode, Candy
// ึᔇᒄ∄喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
// @author fancymouse (http://weibo.com/u/1928162822)
class Solution {
public:
int candy(const vector<int>& ratings) {
vector<int> f(ratings.size());
int sum = 0;
for (int i = 0; i < ratings.size(); ++i)
sum += solve(ratings, f, i);
return sum;
}
int solve(const vector<int>& ratings, vector<int>& f, int i) {
if (f[i] == 0) {
f[i] = 1;
if (i > 0 && ratings[i] > ratings[i - 1])
f[i] = max(f[i], solve(ratings, f, i - 1) + 1);
if (i < ratings.size() - 1 && ratings[i] > ratings[i + 1])
f[i] = max(f[i], solve(ratings, f, i + 1) + 1);
}
return f[i];
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.1.23
Single Number
᣾䔟
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using
extra memory?

---

38
せ2 』
㏮ᕖ㶗
ܵᲿ
ᐱᝅ喌̼ϴ㘬ำ⤵͓⁐⮳ᗴۤ喌ङ㺰ܩ⣟֥᪟⁐喌䘬ञД⌴䰥ȡ
Вⴰ1
// LeetCode, Single Number
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int singleNumber(vector<int>& nums) {
int x = 0;
for (auto i : nums) {
x ^= i;
}
return x;
}
};
Вⴰ2
// LeetCode, Single Number
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int singleNumber(vector<int>& nums) {
return accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
}
};
Ⱗڢ题Ⱍ
• Single Number II, 㻰§2.1.24
2.1.24
Single Number II
᣾䔟
Given an array of integers, every element appears three times except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using
extra memory?
ܵᲿ
ᱛ题঻̹̯题Single Number喌㔲ᄎ⮳᭞Ѽ䓿テȡ
᫨∄1喚݊ᐩ̯͙䪮Ꮥͩ sizeof(int) ⮳᪟㏳count[sizeof(int)]喌count[i] 㶗⹩౗౗i Ѽ
ܩ⣟⮳1 ⮳⁐᪟ȡັ᳋count[i] ᭞3 ⮳᪣᪟Լ喌݈ᔬ⪔喛ॕ݈ᅠឹ䄔ѼअܩᲔ㏳᜿ゃᵷȡ

---

2.1
᪟㏳
39
᫨∄2喚⩗one 䃟ᒄݟᒂݼำ⤵⮳ٲ㉏ͩₑ喌λ䔊ݥ1 ܩ⣟Ć1 ⁐ć喈mod 3 ͺऽ⮳1喉⮳᰸ਙϊ
λ䔊ݥѼ喛⩗two 䃟ᒄݟᒂݼ䃐テ⮳इ䛾ͩₑ喌λ䔊ݥ1 ܩ⣟Ć2 ⁐ć喈mod 3 ͺऽ⮳2喉⮳᰸ਙϊ
λ䔊ݥѼȡᒂone ঻two ͜⮳᳿̯Ѽऻᬥͩ 1 ᬥ㶗⹩䄔λ䔊ݥѼ̹ 1 ܩ⣟ε 3 ⁐喌ₓᬥ䰯㺰⌴䰥ȡ
ࢢ⩗λ䔊ݥὐ᠎̸䔊ݥ䓿テȡᰯ㏷one 䃟ᒄ⮳᭞ᰯ㏷㐂᳋ȡ
Вⴰ1
// LeetCode, Single Number II
// ᫨∄1喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int singleNumber(vector<int>& nums) {
const int W = sizeof(int) * 8; // ̯͙᪣᪟⮳bit ᪟喌ࢢ᪣᪟ႆ䪮
int count[W];
// count[i] 㶗⹩౗౗i Ѽܩ⣟⮳1 ⮳⁐᪟
fill_n(&count[0], W, 0);
for (int i = 0; i < nums.size(); i++) {
for (int j = 0; j < W; j++) {
count[j] += (nums[i] >> j) & 1;
count[j] %= 3;
}
}
int result = 0;
for (int i = 0; i < W; i++) {
result += (count[i] << i);
}
return result;
}
};
Вⴰ2
// LeetCode, Single Number II
// ᫨∄2喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int singleNumber(vector<int>& nums) {
int one = 0, two = 0, three = 0;
for (auto i : nums) {
two |= (one & i);
one ^= i;
three = ~(one & two);
one &= three;
two &= three;
}
return one;
}
};

---

40
せ2 』
㏮ᕖ㶗
Ⱗڢ题Ⱍ
• Single Number, 㻰§2.1.23
2.2
ࢄ䨭㶗
ࢄ䨭㶗㞱◨⮳჉͸ັ̺喚
// ࢄ䨭㶗㞱◨
struct ListNode {
int val;
ListNode *next;
ListNode(int x) : val(x), next(nullptr) { }
};
2.2.1
Add Two Numbers
᣾䔟
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
ܵᲿ
䌎Add Binary喈㻰§3.4喉ᒷㆪѫ
Вⴰ
// LeetCode, Add Two Numbers
// 䌎Add Binary ᒷㆪѫ
// ᬥ䬣฼ᱱᏕO(m+n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
ListNode dummy(-1); // ๣㞱◨
int carry = 0;
ListNode *prev = &dummy;
for (ListNode *pa = l1, *pb = l2;
pa != nullptr || pb != nullptr;
pa = pa == nullptr ? nullptr : pa->next,
pb = pb == nullptr ? nullptr : pb->next,
prev = prev->next) {
const int ai = pa == nullptr ? 0 : pa->val;
const int bi = pb == nullptr ? 0 : pb->val;
const int value = (ai + bi + carry) % 10;
carry = (ai + bi + carry) / 10;

---

2.2
ࢄ䨭㶗
41
prev->next = new ListNode(value); // ᅭᤁ∄
}
if (carry > 0)
prev->next = new ListNode(carry);
return dummy.next;
}
};
Ⱗڢ题Ⱍ
• Add Binary, 㻰§3.4
2.2.2
Reverse Linked List II
᣾䔟
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example: Given 1->2->3->4->5->nullptr, m = 2 and n = 4,
return 1->4->3->2->5->nullptr.
Note: Given m, n satisfy the following condition: 1 ≤m ≤n ≤length of list.
ܵᲿ
䔈题䲍፧㍰⤿喌᰸ᒷ้䓨⩻ᷯᴔ喌15 ܵ䧎ڴ։ݟbug free ᒷ᰸䯭Ꮥ喁
Вⴰ
// LeetCode, Reverse Linked List II
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *reverseBetween(ListNode *head, int m, int n) {
ListNode dummy(-1);
dummy.next = head;
ListNode *prev = &dummy;
for (int i = 0; i < m-1; ++i)
prev = prev->next;
ListNode* const head2 = prev;
prev = head2->next;
ListNode *cur = prev->next;
for (int i = m; i < n; ++i) {
prev->next = cur->next;
cur->next = head2->next;
head2->next = cur;
// ๣ᤁ∄
cur = prev->next;
}

---

42
せ2 』
㏮ᕖ㶗
return dummy.next;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.2.3
Partition List
᣾䔟
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example, Given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5.
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Partition List
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode* partition(ListNode* head, int x) {
ListNode left_dummy(-1); // ๣㐂◨
ListNode right_dummy(-1); // ๣㐂◨
auto left_cur = &left_dummy;
auto right_cur = &right_dummy;
for (ListNode *cur = head; cur; cur = cur->next) {
if (cur->val < x) {
left_cur->next = cur;
left_cur = cur;
} else {
right_cur->next = cur;
right_cur = cur;
}
}
left_cur->next = right_dummy.next;
right_cur->next = nullptr;

---

2.2
ࢄ䨭㶗
43
return left_dummy.next;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.2.4
Remove Duplicates from Sorted List
᣾䔟
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
ܵᲿ
ᬏ
䕁ᒁ❷
// LeetCode, Remove Duplicates from Sorted List
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *deleteDuplicates(ListNode *head) {
if (!head) return head;
ListNode dummy(head->val + 1); // իङ㺰䌎head ̼ऻࢢञ
dummy.next = head;
recur(&dummy, head);
return dummy.next;
}
private:
static void recur(ListNode *prev, ListNode *cur) {
if (cur == nullptr) return;
if (prev->val == cur->val) { // ݏ䮓head
prev->next = cur->next;
delete cur;
recur(prev, prev->next);
} else {
recur(prev->next, cur->next);
}
}
};

---

44
せ2 』
㏮ᕖ㶗
䔜В❷
// LeetCode, Remove Duplicates from Sorted List
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *deleteDuplicates(ListNode *head) {
if (head == nullptr) return nullptr;
for (ListNode *prev = head, *cur = head->next; cur; cur = prev->next) {
if (prev->val == cur->val) {
prev->next = cur->next;
delete cur;
} else {
prev = cur;
}
}
return head;
}
};
Ⱗڢ题Ⱍ
• Remove Duplicates from Sorted List II喌㻰§2.2.5
2.2.5
Remove Duplicates from Sorted List II
᣾䔟
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list.
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
ܵᲿ
ᬏ
䕁ᒁ❷
// LeetCode, Remove Duplicates from Sorted List II
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *deleteDuplicates(ListNode *head) {
if (!head || !head->next) return head;

---

2.2
ࢄ䨭㶗
45
ListNode *p = head->next;
if (head->val == p->val) {
while (p && head->val == p->val) {
ListNode *tmp = p;
p = p->next;
delete tmp;
}
delete head;
return deleteDuplicates(p);
} else {
head->next = deleteDuplicates(head->next);
return head;
}
}
};
䔜В❷
// LeetCode, Remove Duplicates from Sorted List II
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *deleteDuplicates(ListNode *head) {
if (head == nullptr) return head;
ListNode dummy(INT_MIN); // ๣㐂◨
dummy.next = head;
ListNode *prev = &dummy, *cur = head;
while (cur != nullptr) {
bool duplicated = false;
while (cur->next != nullptr && cur->val == cur->next->val) {
duplicated = true;
ListNode *temp = cur;
cur = cur->next;
delete temp;
}
if (duplicated) { // ݏ䮓䛼฼⮳ᰯऽ̯͙ٲ㉏
ListNode *temp = cur;
cur = cur->next;
delete temp;
continue;
}
prev->next = cur;
prev = prev->next;
cur = cur->next;
}
prev->next = cur;
return dummy.next;
}
};

---

46
せ2 』
㏮ᕖ㶗
Ⱗڢ题Ⱍ
• Remove Duplicates from Sorted List喌㻰§2.2.4
2.2.6
Rotate List
᣾䔟
Given a list, rotate the list to the right by k places, where k is non-negative.
For example: Given 1->2->3->4->5->nullptr and k = 2, return 4->5->1->2->3->nullptr.
ܵᲿ
ٷ䕼ࢵ̯䕼喌ᓆܩ䨭㶗䪮Ꮥlen喌∗ᘾk ञ㘬๖ν len喌ఏₓГ k% = lenȡᄵᅭ㞱◨next ᠶ䦷
ᠶी仅㞱◨喌ᒑ᜿̯͙⣞喌ᣔⱯᒯऽ䌀len −k ₔ喌Ͻ䔈䛻᫜ᐯ喌ᅠ᭞㺰ⅱ⮳㐂᳋εȡ
Вⴰ
// LeetCode, Remove Rotate List
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *rotateRight(ListNode *head, int k) {
if (head == nullptr || k == 0) return head;
int len = 1;
ListNode* p = head;
while (p->next) { // ⅱ䪮Ꮥ
len++;
p = p->next;
}
k = len - k % len;
p->next = head; // 仅ᅭⰧ䔍
for(int step = 0; step < k; step++) {
p = p->next;
//ᣔⱯᒯऽ䌀
}
head = p->next; // ᫟⮳仅㞱◨
p->next = nullptr; // ᫜ᐯ⣞
return head;
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

2.2
ࢄ䨭㶗
47
2.2.7
Remove Nth Node From End of List
᣾䔟
Given a linked list, remove the nth node from the end of list and return its head.
For example, Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
• Given n will always be valid.
• Try to do this in one pass.
ܵᲿ
䃭͓͙ᠶ䦷p, q喌䃘q ٷ䊟n ₔ喌♥ऽp ঻q ̯䊦䊟喌Ⱓݟq 䊟ݟᅭ㞱◨喌ݏ䮓p->next ࢢञȡ
Вⴰ
// LeetCode, Remove Nth Node From End of List
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *removeNthFromEnd(ListNode *head, int n) {
ListNode dummy{-1, head};
ListNode *p = &dummy, *q = &dummy;
for (int i = 0; i < n; i++)
// q ٷ䊟n ₔ
q = q->next;
while(q->next) { // ̯䊦䊟
p = p->next;
q = q->next;
}
ListNode *tmp = p->next;
p->next = p->next->next;
delete tmp;
return dummy.next;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.2.8
Swap Nodes in Pairs
᣾䔟
Given a linked list, swap every two adjacent nodes and return its head.

---

48
せ2 』
㏮ᕖ㶗
For example, Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes
itself can be changed.
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Swap Nodes in Pairs
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *swapPairs(ListNode *head) {
if (head == nullptr || head->next == nullptr) return head;
ListNode dummy(-1);
dummy.next = head;
for(ListNode *prev = &dummy, *cur = prev->next, *next = cur->next;
next;
prev = cur, cur = cur->next, next = cur ? cur->next: nullptr) {
prev->next = next;
cur->next = next->next;
next->next = cur;
}
return dummy.next;
}
};
̺䲑䔈⻼ۈ∄ᰣク∰喌ѵ题Ⱍ㻳჉ε̼۵䔈ᵦ։ȡ
// LeetCode, Swap Nodes in Pairs
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode* swapPairs(ListNode* head) {
ListNode* p = head;
while (p && p->next) {
swap(p->val, p->next->val);
p = p->next->next;
}
return head;
}
};
Ⱗڢ题Ⱍ
• Reverse Nodes in k-Group, 㻰§2.2.9

---

2.2
ࢄ䨭㶗
49
2.2.9
Reverse Nodes in k-Group
᣾䔟
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
For example, Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
ܵᲿ
ᬏ
䕁ᒁ❷
// LeetCode, Reverse Nodes in k-Group
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *reverseKGroup(ListNode *head, int k) {
if (head == nullptr || head->next == nullptr || k < 2)
return head;
ListNode *next_group = head;
for (int i = 0; i < k; ++i) {
if (next_group)
next_group = next_group->next;
else
return head;
}
// next_group is the head of next group
// new_next_group is the new head of next group after reversion
ListNode *new_next_group = reverseKGroup(next_group, k);
ListNode *prev = NULL, *cur = head;
while (cur != next_group) {
ListNode *next = cur->next;
cur->next = prev ? prev : new_next_group;
prev = cur;
cur = next;
}
return prev; // prev will be the new head of this group
}
};

---

50
せ2 』
㏮ᕖ㶗
䔜В❷
// LeetCode, Reverse Nodes in k-Group
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *reverseKGroup(ListNode *head, int k) {
if (head == nullptr || head->next == nullptr || k < 2) return head;
ListNode dummy(-1);
dummy.next = head;
for(ListNode *prev = &dummy, *end = head; end; end = prev->next) {
for (int i = 1; i < k && end; i++)
end = end->next;
if (end
== nullptr) break;
// ̼䋢k ͙
prev = reverse(prev, prev->next, end);
}
return dummy.next;
}
// prev ᭞first ݼ̯͙ٲ㉏, [begin, end] 䬜ࡩ䬣喌Ԍ䃰̸㔴䘬̼ͩ null
// 䔃఍ࣼ䒛ऽ⮳Ձ᪟せ1 ͙ٲ㉏
ListNode* reverse(ListNode *prev, ListNode *begin, ListNode *end) {
ListNode *end_next = end->next;
for (ListNode *p = begin, *cur = p->next, *next = cur->next;
cur != end_next;
p = cur, cur = next, next = next ? next->next : nullptr) {
cur->next = p;
}
begin->next = end_next;
prev->next = end;
return begin;
}
};
Ⱗڢ题Ⱍ
• Swap Nodes in Pairs, 㻰§2.2.8
2.2.10
Copy List with Random Pointer
᣾䔟
A linked list is given such that each node contains an additional random pointer which could point to
any node in the list or null.
Return a deep copy of the list.

---

2.2
ࢄ䨭㶗
51
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Copy List with Random Pointer
// ͓䕼រ᣾喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
RandomListNode *copyRandomList(RandomListNode *head) {
for (RandomListNode* cur = head; cur != nullptr; ) {
RandomListNode* node = new RandomListNode(cur->label);
node->next = cur->next;
cur->next = node;
cur = node->next;
}
for (RandomListNode* cur = head; cur != nullptr; ) {
if (cur->random != NULL)
cur->next->random = cur->random->next;
cur = cur->next->next;
}
// ܵ៵͓͙ࢄ䨭㶗
RandomListNode dummy(-1);
for (RandomListNode* cur = head, *new_cur = &dummy;
cur != nullptr; ) {
new_cur->next = cur->next;
new_cur = new_cur->next;
cur->next = cur->next->next;
cur = cur->next;
}
return dummy.next;
}
};
Ⱗڢ题Ⱍ
• ᬏ
2.2.11
Linked List Cycle
᣾䔟
Given a linked list, determine if it has a cycle in it.
Follow up: Can you solve it without using extra space?

---

52
せ2 』
㏮ᕖ㶗
ܵᲿ
ᰯშᭂᘢݟ⮳᫨∄᭞喌⩗̯͙৷ጻ㶗unordered_map<int, bool> visited喌䃟ᒄ⃾͙ٲ㉏᭞
ॕ㷚䃮䬝䓶喌̯ᬕܩ⣟᳿͙ٲ㉏㷚䛼฼䃮䬝喌䄣ᬽႇ౗⣞ȡ⾩䬣฼ᱱᏕO(n)喌ᬥ䬣฼ᱱᏕO(N)ȡ
ᰯຬ⮳᫨∄᭞ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1) ⮳ȡ䃭㒝͓͙ᠶ䦷喌̯͙ᔚ̯͙ᚑ喌
ᔚ⮳ᠶ䦷⃾⁐䊟͓ₔ喌ᚑ⮳ᠶ䦷⃾⁐䊟̯ₔ喌ັ᳋ᔚᠶ䦷঻ᚑᠶ䦷Ⱗ䕶喌݈䄣ᬽ᰸⣞ȡࣱ㔲
http://leetcode.com/2010/09/detecting-loop-in-singly-linked-list.html
Вⴰ
//LeetCode, Linked List Cycle
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool hasCycle(ListNode *head) {
// 䃭㒝͓͙ᠶ䦷喌̯͙ᔚ̯͙ᚑ
ListNode *slow = head, *fast = head;
while (fast && fast->next) {
slow = slow->next;
fast = fast->next->next;
if (slow == fast) return true;
}
return false;
}
};
Ⱗڢ题Ⱍ
• Linked List Cycle II, 㻰§2.2.12
2.2.12
Linked List Cycle II
᣾䔟
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Follow up: Can you solve it without using extra space?
ܵᲿ
ᒂfast ̽ slow Ⱗ䕶ᬥ喌slow 㗞჉⇐᰸䕼ࢵႻ䨭㶗喌㔻fast ጡ㏾౗⣞ڴᓙ⣞ε n ష(1 ≤n)ȡն
䃭slow 䊟ε s ₔ喌݈fast 䊟ε 2s ₔ喈fast ₔ᪟䔇へν s ߏ̹౗⣞้̹䒛⮳n ష喉喌䃭⣞䪮ͩ r喌݈喚
2s
=
s + nr
s
=
nr

---

2.2
ࢄ䨭㶗
53
䃭᪣͙䨭㶗䪮L喌⣞ڔऒ◨̽Ⱗ䕶◨䌌⻪ͩ a喌䊦◨ݟ⣞ڔऒ◨⮳䌌⻪ͩ x喌݈
x + a
=
nr = (n–1)r + r = (n −1)r + L −x
x
=
(n −1)r + (L–x–a)
L–x–a ͩⰧ䕶◨ݟ⣞ڔऒ◨⮳䌌⻪喌⩠ₓञⴔ喌Ͻ䨭㶗๣ݟ⣞ڔऒ◨へν n −1 షڴ⣞+ Ⱗ䕶
◨ݟ⣞ڔऒ◨喌ν᭞ᝀЛञДϽ head ᐯ໺क䃭̯͙ᠶ䦷slow2喌͓͙ᚑᠶ䦷⃾⁐ݼ䔊̯ₔ喌ႲԘ
̯჉щ౗⣞ڔऒ◨Ⱗ䕶ȡ
Вⴰ
//LeetCode, Linked List Cycle II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *detectCycle(ListNode *head) {
ListNode *slow = head, *fast = head;
while (fast && fast->next) {
slow = slow->next;
fast = fast->next->next;
if (slow == fast) {
ListNode *slow2 = head;
while (slow2 != slow) {
slow2 = slow2->next;
slow = slow->next;
}
return slow2;
}
}
return nullptr;
}
};
Ⱗڢ题Ⱍ
• Linked List Cycle, 㻰§2.2.11
2.2.13
Reorder List
᣾䔟
Given a singly linked list L : L0 →L1 →· · · →Ln−1 →Ln, reorder it to: L0 →Ln →L1 →
Ln−1 →L2 →Ln−2 →· · ·
You must do this in-place without altering the nodes’ values.
For example, Given {1,2,3,4}, reorder it to {1,4,2,3}.

---

54
せ2 』
㏮ᕖ㶗
ܵᲿ
题Ⱍ㻳჉㺰in-place喌Ύᅠ᭞䄣ङ㘬Ү⩗O(1) ⮳⾩䬣ȡ
ञДឭݟ͜䬣㞱◨喌᫜ᐯ喌ឹऽࡹ᝙ࢄ䨭㶗reverse ̯̺喌ڼषᎥ͓͙ࢄ䨭㶗ȡ
Вⴰ
// LeetCode, Reorder List
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void reorderList(ListNode *head) {
if (head == nullptr || head->next == nullptr) return;
ListNode *slow = head, *fast = head, *prev = nullptr;
while (fast && fast->next) {
prev = slow;
slow = slow->next;
fast = fast->next->next;
}
prev->next = nullptr; // cut at middle
slow = reverse(slow);
// merge two lists
ListNode *curr = head;
while (curr->next) {
ListNode *tmp = curr->next;
curr->next = slow;
slow = slow->next;
curr->next->next = tmp;
curr = tmp;
}
curr->next = slow;
}
ListNode* reverse(ListNode *head) {
if (head == nullptr || head->next == nullptr) return head;
ListNode *prev = head;
for (ListNode *curr = head->next, *next = curr->next; curr;
prev = curr, curr = next, next = next ? next->next : nullptr) {
curr->next = prev;
}
head->next = nullptr;
return prev;
}
};

---

2.2
ࢄ䨭㶗
55
Ⱗڢ题Ⱍ
• ᬏ
2.2.14
LRU Cache
᣾䔟
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
following operations: get and set.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise
return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its
capacity, it should invalidate the least recently used item before inserting a new item.
ܵᲿ
ͩεҮᴔឭȠᤁڔ঻ݏ䮓䘬᰸䒲倇⮳ᕖ㘬喌ᝀЛҮ⩗̯͙ࣻी䨭㶗(std::list) ঻̯͙৷ጻ㶗
(std::unordered_map)喌ఏͩ喚
• ৷ጻ㶗Ԍႇ⃾͙㞱◨⮳౟౯喌ञДഩᱛԌ䃰౗O(1) ᬥ䬣ڴᴔឭ㞱◨
• ࣻी䨭㶗ᤁڔ঻ݏ䮓᩷⢶倇喌ࢄी䨭㶗ᤁڔ঻ݏ䮓ᬥ喌䔇㺰ᴔឭ㞱◨⮳ݼ侠㞱◨
ڦ҂Ⴭ⣟㏵㞱喚
• 䊹䲏䔀䨭㶗๣䘗喌㶗⹩㞱◨̹⁐䃮䬝䌌⻪⣟౗ᬥ䬣ᰯⴜ喌ᅭ䘗⮳㞱◨㶗⹩ᰯ䔀䃮䬝ᰯᅀ
• 䃮䬝㞱◨ᬥ喌ັ᳋㞱◨ႇ౗喌ឹ䄔㞱◨ϓᢑݟ䨭㶗๣䘗喌ऻᬥᰣ᫟hash 㶗͜䄔㞱◨⮳౟౯
• ᤁڔ㞱◨ᬥ喌ັ᳋cache ⮳size 䓭ݟε̹䭿capacity喌݈ݏ䮓ᅭ䘗㞱◨喌ऻᬥ㺰౗hash 㶗͜ݏ
䮓ᄨᏃ⮳䶨喛᫟㞱◨ᤁڔ䨭㶗๣䘗
Вⴰ
// LeetCode, LRU Cache
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(n)
class LRUCache{
private:
struct CacheNode {
int key;
int value;
CacheNode(int k, int v) :key(k), value(v){}
};
public:
LRUCache(int capacity) {
this->capacity = capacity;
}

---

56
せ2 』
㏮ᕖ㶗
int get(int key) {
if (cacheMap.find(key) == cacheMap.end()) return -1;
// ឹᒂݼ䃮䬝⮳㞱◨⼪ݟ䨭㶗๣䘗喌Ꭵ̓ᰣ᫟map ͜䄔㞱◨⮳౟౯
cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
cacheMap[key] = cacheList.begin();
return cacheMap[key]->value;
}
void set(int key, int value) {
if (cacheMap.find(key) == cacheMap.end()) {
if (cacheList.size() == capacity) { //ݏ䮓䨭㶗ᅭ䘗㞱◨喈ᰯᅀ䃮䬝⮳㞱◨喉
cacheMap.erase(cacheList.back().key);
cacheList.pop_back();
}
// ᤁڔ᫟㞱◨ݟ䨭㶗๣䘗, Ꭵ̓౗map ͜෍ߏ䄔㞱◨
cacheList.push_front(CacheNode(key, value));
cacheMap[key] = cacheList.begin();
} else {
//ᰣ᫟㞱◨⮳ի喌ឹᒂݼ䃮䬝⮳㞱◨⼪ݟ䨭㶗๣䘗, Ꭵ̓ᰣ᫟map ͜䄔㞱◨⮳౟౯
cacheMap[key]->value = value;
cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
cacheMap[key] = cacheList.begin();
}
}
private:
list<CacheNode> cacheList;
unordered_map<int, list<CacheNode>::iterator> cacheMap;
int capacity;
};
Ⱗڢ题Ⱍ
• ᬏ

---

せ3 』
ႆさ͡
3.1
Valid Palindrome
᣾䔟
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring
cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note: Have you consider that the string might be empty? This is a good question to ask during an
interview.
For the purpose of this problem, we define empty string as valid palindrome.
ܵᲿ
ᬏ
Вⴰ
// Leet Code, Valid Palindrome
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool isPalindrome(string s) {
transform(s.begin(), s.end(), s.begin(), ::tolower);
auto left = s.begin(), right = prev(s.end());
while (left < right) {
if (!::isalnum(*left))
++left;
else if (!::isalnum(*right)) --right;
else if (*left != *right) return false;
else { left++, right--; }
}
return true;
}
};
57

---

58
せ3 』
ႆさ͡
Ⱗڢ题Ⱍ
• Palindrome Number, 㻰§15.2
3.2
Implement strStr()
᣾䔟
Implement strStr().
Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
ܵᲿ
ᯣߊテ∄⮳฼ᱱᏕ᭞O(m ∗n)喌Вⴰັ̺ȡᰣ倇᩷⮳⮳テ∄᰸KMP テ∄ȠBoyer-Mooer テ∄঻
Rabin-Karp テ∄ȡ䲑䄄͜ᯣߊテ∄䋢๎ε喌̯჉㺰ۈᓆ⇐᰸BUGȡ
ᯣߊࡨ䙼
// LeetCode, Implement strStr()
// ᯣߊ解∄喌ᬥ䬣฼ᱱᏕO(N*M)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int strStr(const string& haystack, const string& needle) {
if (needle.empty()) return 0;
const int N = haystack.size() - needle.size() + 1;
for (int i = 0; i < N; i++) {
int j = i;
int k = 0;
while (j < haystack.size() && k < needle.size() && haystack[j] == needle[k]) {
j++;
k++;
}
if (k == needle.size()) return i;
}
return -1;
}
};
KMP
// LeetCode, Implement strStr()
// KMP喌ᬥ䬣฼ᱱᏕO(N+M)喌⾩䬣฼ᱱᏕO(M)
class Solution {
public:
int strStr(const string& haystack, const string& needle) {
return kmp(haystack.c_str(), needle.c_str());
}

---

3.2
Implement strStr()
59
private:
/*
* @brief 䃐テ䘗ܵࡨ䙼㶗喌ࢢnext ᪟㏳.
*
* @param[in] pattern ὐᐾ͡
* @param[out] next next ᪟㏳
* @return ᬏ
*/
static void compute_prefix(const char *pattern, int next[]) {
int i;
int j = -1;
const int m = strlen(pattern);
next[0] = j;
for (i = 1; i < m; i++) {
while (j > -1 && pattern[j + 1] != pattern[i]) j = next[j];
if (pattern[i] == pattern[j + 1]) j++;
next[i] = j;
}
}
/*
* @brief KMP テ∄.
*
* @param[in] text ᪶ᱛ
* @param[in] pattern ὐᐾ͡
* @return ᜿ߎ݈䔃఍せ̯⁐ࡨ䙼⮳Ѽ㒝喌๠䉔݈䔃఍-1
*/
static int kmp(const char *text, const char *pattern) {
int i;
int j = -1;
const int n = strlen(text);
const int m = strlen(pattern);
if (n == 0 && m == 0) return 0; /* "","" */
if (m == 0) return 0;
/* "a","" */
int *next = (int*)malloc(sizeof(int) * m);
compute_prefix(pattern, next);
for (i = 0; i < n; i++) {
while (j > -1 && pattern[j + 1] != text[i]) j = next[j];
if (text[i] == pattern[j + 1]) j++;
if (j == m - 1) {
free(next);
return i-j;
}
}
free(next);
return -1;
}

---

60
せ3 』
ႆさ͡
};
Ⱗڢ题Ⱍ
• String to Integer (atoi) 喌㻰§3.3
3.3
String to Integer (atoi)
᣾䔟
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and
ask yourself what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are respon-
sible to gather all the input requirements up front.
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace
character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by
as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored
and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such
sequence exists because either str is empty or it contains only whitespace characters, no conversion is per-
formed.
If no valid conversion could be performed, a zero value is returned. If the correct value is out of the
range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
ܵᲿ
㏵㞱题ȡ∗ᘾ܏͙≺䄄⩗Һ喚
1. ̼㻳݈䓂ڔ喌ѵ᭞᰸᩷喌”-3924x8fc”喌” + 413”,
2. ᬏ᩷ᵫᐾ喌” ++c”, ” ++1”
3. ⏑ܩ᪟ᢝ喌”2147483648”
Вⴰ
// LeetCode, String to Integer (atoi)
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {

---

3.4
Add Binary
61
public:
int myAtoi(const string &str) {
int num = 0;
int sign = 1;
const int n = str.length();
int i = 0;
while (str[i] == ' ' && i < n) i++;
if (str[i] == '+') {
i++;
} else if (str[i] == '-') {
sign = -1;
i++;
}
for (; i < n; i++) {
if (str[i] < '0' || str[i] > '9')
break;
if (num > INT_MAX / 10 ||
(num == INT_MAX / 10 &&
(str[i] - '0') > INT_MAX % 10)) {
return sign == -1 ? INT_MIN : INT_MAX;
}
num = num * 10 + str[i] - '0';
}
return num * sign;
}
};
Ⱗڢ题Ⱍ
• Implement strStr() 喌㻰§3.2
3.4
Add Binary
᣾䔟
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
ܵᲿ
ᬏ

---

62
せ3 』
ႆさ͡
Вⴰ
//LeetCode, Add Binary
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
string addBinary(string a, string b) {
string result;
const size_t n = a.size() > b.size() ? a.size() : b.size();
reverse(a.begin(), a.end());
reverse(b.begin(), b.end());
int carry = 0;
for (size_t i = 0; i < n; i++) {
const int ai = i < a.size() ? a[i] - '0' : 0;
const int bi = i < b.size() ? b[i] - '0' : 0;
const int val = (ai + bi + carry) % 2;
carry = (ai + bi + carry) / 2;
result.insert(result.begin(), val + '0');
}
if (carry == 1) {
result.insert(result.begin(), '1');
}
return result;
}
};
Ⱗڢ题Ⱍ
• Add Two Numbers, 㻰§2.2.1
3.5
Longest Palindromic Substring
᣾䔟
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length
of S is 1000, and there exists one unique longest palindromic substring.
ܵᲿ
ᰯ䪮఍᪶ၿ͡喌䲍፧㏾ڧ⮳题ȡ
ᕌ䌞̯喚ᯣߊ᳉ͭ喌Д⃾͙ٲ㉏ͩ͜䬣ٲ㉏喌ऻᬥϽጕढܩऀ喌฼ᱱᏕO(n2)ȡ
ᕌ䌞λ喚䃟ᓵࡅ᥋㉑喌฼ᱱᏕO(n2)ȡ䃭f[i][j] 㶗⹩[i,j] ͺ䬣⮳ᰯ䪮఍᪶ၿ͡喌䕁ᣗ᫨⼺ັ
̺喚
f[i][j] = if (i == j) S[i]
if (S[i] == S[j] && f[i+1][j-1] == S[i+1][j-1]) S[i][j]
else max(f[i+1][j-1], f[i][j-1], f[i+1][j])

---

3.5
Longest Palindromic Substring
63
ᕌ䌞̸喚ߗ㻳喌฼ᱱᏕO(n2)ȡ䃭⟥ᔰͩ f(i,j)喌㶗⹩ࡩ䬣[i,j] ᭞ॕͩ఍᪶͡喌݈⟥ᔰ䒛⼪᫨
⼺ͩ
f(i, j) =









true
, i = j
S[i] = S[j]
, j = i + 1
S[i] = S[j] and f(i + 1, j −1)
, j > i + 1
ᕌ䌞ఊ喚Manacherąs Algorithm, ฼ᱱᏕO(n)ȡ䄕㏵解䛹㻰http://leetcode.com/2011/11/longest-
palindromic-substring-part-ii.html ȡ
ึᔇᒄ∄
// LeetCode, Longest Palindromic Substring
// ึᔇᒄ∄喌щ䊴ᬥ
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
typedef string::const_iterator Iterator;
namespace std {
template<>
struct hash<pair<Iterator, Iterator>> {
size_t operator()(pair<Iterator, Iterator> const& p) const {
return ((size_t) &(*p.first)) ^ ((size_t) &(*p.second));
}
};
}
class Solution {
public:
string longestPalindrome(string const& s) {
cache.clear();
return cachedLongestPalindrome(s.begin(), s.end());
}
private:
unordered_map<pair<Iterator, Iterator>, string> cache;
string longestPalindrome(Iterator first, Iterator last) {
size_t length = distance(first, last);
if (length < 2) return string(first, last);
auto s = cachedLongestPalindrome(next(first), prev(last));
if (s.length() == length - 2 && *first == *prev(last))
return string(first, last);
auto s1 = cachedLongestPalindrome(next(first), last);
auto s2 = cachedLongestPalindrome(first, prev(last));
// return max(s, s1, s2)
if (s.size() > s1.size()) return s.size() > s2.size() ? s : s2;

---

64
せ3 』
ႆさ͡
else return s1.size() > s2.size() ? s1 : s2;
}
string cachedLongestPalindrome(Iterator first, Iterator last) {
auto key = make_pair(first, last);
auto pos = cache.find(key);
if (pos != cache.end()) return pos->second;
else return cache[key] = longestPalindrome(first, last);
}
};
ߗ㻳
// LeetCode, Longest Palindromic Substring
// ߗ㻳喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
string longestPalindrome(const string& s) {
const int n = s.size();
bool f[n][n];
fill_n(&f[0][0], n * n, false);
// ⩗vector щ䊴ᬥ
//vector<vector<bool> > f(n, vector<bool>(n, false));
size_t max_len = 1, start = 0;
// ᰯ䪮఍᪶ၿ͡⮳䪮Ꮥ喌䊦◨
for (size_t i = 0; i < s.size(); i++) {
f[i][i] = true;
for (size_t j = 0; j < i; j++) {
// [j, i]
f[j][i] = (s[j] == s[i] && (i - j < 2 || f[j + 1][i - 1]));
if (f[j][i] && max_len < (i - j + 1)) {
max_len = i - j + 1;
start = j;
}
}
}
return s.substr(start, max_len);
}
};
Manacherąs Algorithm
// LeetCode, Longest Palindromic Substring
// Manacherąs Algorithm
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
// Transform S into T.
// For example, S = "abba", T = "^#a#b#b#a#$".
// ^ and $ signs are sentinels appended to each end to avoid bounds checking
string preProcess(const string& s) {
int n = s.length();

---

3.5
Longest Palindromic Substring
65
if (n == 0) return "^$";
string ret = "^";
for (int i = 0; i < n; i++) ret += "#" + s.substr(i, 1);
ret += "#$";
return ret;
}
string longestPalindrome(string s) {
string T = preProcess(s);
const int n = T.length();
// Д T[i] ͩ͜ᓲ喌ीጕ/ढមᑏ⮳䪮Ꮥ喌̼࠴ग़T[i] 㜙ጠ喌
// ఏₓ P[i] ᭞⎿ႆさ͜͡఍᪶͡⮳䪮Ꮥ
int P[n];
int C = 0, R = 0;
for (int i = 1; i < n - 1; i++) {
int i_mirror = 2 * C - i; // equals to i' = C - (i-C)
P[i] = (R > i) ? min(R - i, P[i_mirror]) : 0;
// Attempt to expand palindrome centered at i
while (T[i + 1 + P[i]] == T[i - 1 - P[i]])
P[i]++;
// If palindrome centered at i expand past R,
// adjust center based on expanded palindrome.
if (i + P[i] > R) {
C = i;
R = i + P[i];
}
}
// Find the maximum element in P.
int max_len = 0;
int center_index = 0;
for (int i = 1; i < n - 1; i++) {
if (P[i] > max_len) {
max_len = P[i];
center_index = i;
}
}
return s.substr((center_index - 1 - max_len) / 2, max_len);
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

66
せ3 』
ႆさ͡
3.6
Regular Expression Matching
᣾䔟
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character. '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") →false
isMatch("aa","aa") →true
isMatch("aaa","aa") →false
isMatch("aa", "a*") →true
isMatch("aa", ".*") →true
isMatch("ab", ".*") →true
isMatch("aab", "c*a*b") →true
ܵᲿ
䔈᭞̯䖂ᒷ᰸ᡀᝇ⮳题ȡ
䕁ᒁ❷
// LeetCode, Regular Expression Matching
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool isMatch(const string& s, const string& p) {
return isMatch(s.c_str(), p.c_str());
}
private:
bool isMatch(const char *s, const char *p) {
if (*p == '\0') return *s == '\0';
// next char is not '*', then must match current character
if (*(p + 1) != '*') {
if (*p == *s || (*p == '.' && *s != '\0'))
return isMatch(s + 1, p + 1);
else
return false;
} else { // next char is '*'
while (*p == *s || (*p == '.' && *s != '\0')) {
if (isMatch(s, p + 2))
return true;
s++;
}
return isMatch(s, p + 2);

---

3.7
Wildcard Matching
67
}
}
};
䔜В❷
Ⱗڢ题Ⱍ
• Wildcard Matching, 㻰§3.7
3.7
Wildcard Matching
᣾䔟
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character. '*' Matches any sequence of characters (including the empty se-
quence).
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") →false
isMatch("aa","aa") →true
isMatch("aaa","aa") →false
isMatch("aa", "*") →true
isMatch("aa", "a*") →true
isMatch("ab", "?*") →true
isMatch("aab", "c*a*b") →false
ܵᲿ
䌎̹̯题ᒷㆪѫȡ
ͪ㺰᭞'*' ⮳ࡨ䙼䬝题ȡp ⃾䕶ݟ̯͙'*'喌ᅠԌ⪈Ѿᒂݼ'*' ⮳౿ᴶ঻s ⮳౿ᴶ喌♥ऽs Ͻݼ
ᒯऽរ᣾喌ັ᳋̼᜿ߎ喌݈s++喌䛼᫟រ᣾ȡ
䕁ᒁ❷
// LeetCode, Wildcard Matching
// 䕁ᒁ❷喌щ䊴ᬥ喌⩗ν፝ߘ⤵解题ᘾ
// ᬥ䬣฼ᱱᏕO(n!*m!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:

---

68
せ3 』
ႆさ͡
bool isMatch(const string& s, const string& p) {
return isMatch(s.c_str(), p.c_str());
}
private:
bool isMatch(const char *s, const char *p) {
if (*p == '*') {
while (*p == '*') ++p;
//skip continuous '*'
if (*p == '\0') return true;
while (*s != '\0' && !isMatch(s, p)) ++s;
return *s != '\0';
}
else if (*p == '\0' || *s == '\0') return *p == *s;
else if (*p == *s || *p == '?') return isMatch(++s, ++p);
else return false;
}
};
䔜В❷
// LeetCode, Wildcard Matching
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n*m)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool isMatch(const string& s, const string& p) {
return isMatch(s.c_str(), p.c_str());
}
private:
bool isMatch(const char *s, const char *p) {
bool star = false;
const char *str, *ptr;
for (str = s, ptr = p; *str != '\0'; str++, ptr++) {
switch (*ptr) {
case '?':
break;
case '*':
star = true;
s = str, p = ptr;
while (*p == '*') p++;
//skip continuous '*'
if (*p == '\0') return true;
str = s - 1;
ptr = p - 1;
break;
default:
if (*str != *ptr) {
// ັ᳋ݼ䲑⇐᰸'*'喌݈ࡨ䙼̼᜿ߎ
if (!star) return false;
s++;
str = s - 1;
ptr = p - 1;
}
}
}

---

3.8
Longest Common Prefix
69
while (*ptr == '*') ptr++;
return (*ptr == '\0');
}
};
Ⱗڢ题Ⱍ
• Regular Expression Matching, 㻰§3.6
3.8
Longest Common Prefix
᣾䔟
Write a function to find the longest common prefix string amongst an array of strings.
ܵᲿ
ϽѼ㒝0 ᐯ໺喌ᄨ⃾̯͙Ѽ㒝℃䒲ᝯ᰸ႆさ͡喌Ⱓݟ䕶ݟ̯͙̼ࡨ䙼ȡ
㏤ीរ᣾
// LeetCode, Longest Common Prefix
// ㏤ीរ᣾喌ϽѼ㒝0 ᐯ໺喌ᄨ⃾̯͙Ѽ㒝℃䒲ᝯ᰸ႆさ͡喌Ⱓݟ䕶ݟ̯͙̼ࡨ䙼
// ᬥ䬣฼ᱱᏕO(n1+n2+...)
// @author গ՘ (http://weibo.com/zhouditty)
class Solution {
public:
string longestCommonPrefix(vector<string> &strs) {
if (strs.empty()) return "";
for (int idx = 0; idx < strs[0].size(); ++idx) { // ㏤ीរ᣾
for (int i = 1; i < strs.size(); ++i) {
if (strs[i][idx] != strs[0][idx]) return strs[0].substr(0,idx);
}
}
return strs[0];
}
};
Ὑीរ᣾
// LeetCode, Longest Common Prefix
// Ὑीរ᣾喌⃾͙ႆさ̽͡せ0 ͙ႆさ͡喌Ͻጕݟढ℃䒲喌Ⱓݟ䕶ݟ̯͙̼ࡨ䙼喌
// ♥ऽ㐖㐜̺̯͙ႆさ͡
// ᬥ䬣฼ᱱᏕO(n1+n2+...)
class Solution {
public:
string longestCommonPrefix(vector<string> &strs) {

---

70
せ3 』
ႆさ͡
if (strs.empty()) return "";
int right_most = strs[0].size() - 1;
for (size_t i = 1; i < strs.size(); i++)
for (int j = 0; j <= right_most; j++)
if (strs[i][j] != strs[0][j])
// ̼щ䊹⩻喌䄦ࣱ㔲string::[] ⮳᪶ᶒ
right_most = j - 1;
return strs[0].substr(0, right_most + 1);
}
};
Ⱗڢ题Ⱍ
• ᬏ
3.9
Valid Number
᣾䔟
Validate if a given string is numeric.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up
front before implementing one.
ܵᲿ
㏵㞱Ⴭ⣟题ȡ
ᱛ题⮳ߎ㘬̽ᴶ۵Ꮒ͜⮳strtod() ߎ㘬ㆪѫȡ
᰸䭿㜙ߗᱩ
// LeetCode, Valid Number
// @author 哉䭵Ⴘ(http://weibo.com/luangong)
// finite automata喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
bool isNumber(const string& s) {
enum InputType {
INVALID,
// 0
SPACE,
// 1

---

3.9
Valid Number
71
SIGN,
// 2
DIGIT,
// 3
DOT,
// 4
EXPONENT,
// 5
NUM_INPUTS
// 6
};
const int transitionTable[][NUM_INPUTS] = {
-1, 0, 3, 1, 2, -1, // next states for state 0
-1, 8, -1, 1, 4, 5,
// next states for state 1
-1, -1, -1, 4, -1, -1,
// next states for state 2
-1, -1, -1, 1, 2, -1,
// next states for state 3
-1, 8, -1, 4, -1, 5,
// next states for state 4
-1, -1, 6, 7, -1, -1,
// next states for state 5
-1, -1, -1, 7, -1, -1,
// next states for state 6
-1, 8, -1, 7, -1, -1,
// next states for state 7
-1, 8, -1, -1, -1, -1,
// next states for state 8
};
int state = 0;
for (auto ch : s) {
InputType inputType = INVALID;
if (isspace(ch))
inputType = SPACE;
else if (ch == '+' || ch == '-')
inputType = SIGN;
else if (isdigit(ch))
inputType = DIGIT;
else if (ch == '.')
inputType = DOT;
else if (ch == 'e' || ch == 'E')
inputType = EXPONENT;
// Get next state from current state and input symbol
state = transitionTable[state][inputType];
// Invalid input
if (state == -1) return false;
}
// If the current state belongs to one of the accepting (final) states,
// then the number is valid
return state == 1 || state == 4 || state == 7 || state == 8;
}
};
Ү⩗strtod()
// LeetCode, Valid Number
// @author 䔍೽(http://weibo.com/lianchengzju)
// ֦ᜁ喌Ⱓᣔ⩗strtod()喌ᬥ䬣฼ᱱᏕO(n)
class Solution {
public:
bool isNumber (const string& s) {

---

72
せ3 』
ႆさ͡
return isNumber(s.c_str());
}
private:
bool isNumber (char const* s) {
char* endptr;
strtod (s, &endptr);
if (endptr == s) return false;
for (; *endptr; ++endptr)
if (!isspace (*endptr)) return false;
return true;
}
};
Ⱗڢ题Ⱍ
• ᬏ
3.10
Integer to Roman
᣾䔟
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Integer to Roman
// ᬥ䬣฼ᱱᏕO(num)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
string intToRoman(int num) {
const int radix[] = {1000, 900, 500, 400, 100, 90,
50, 40, 10, 9, 5, 4, 1};
const string symbol[] = {"M", "CM", "D", "CD", "C", "XC",
"L", "XL", "X", "IX", "V", "IV", "I"};
string roman;
for (size_t i = 0; num > 0; ++i) {
int count = num / radix[i];
num %= radix[i];
for (; count > 0; --count) roman += symbol[i];

---

3.11
Roman to Integer
73
}
return roman;
}
};
Ⱗڢ题Ⱍ
• Roman to Integer, 㻰§3.11
3.11
Roman to Integer
᣾䔟
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
ܵᲿ
Ͻݼᒯऽរ᣾喌⩗̯͙ͣᬥइ䛾䃟ᒄܵ⃤᪟ႆȡ
ັ᳋ᒂݼ℃ݼ̯͙๖喌䄣ᬽ䔈̯⃤⮳իᏃ䄔᭞ᒂݼ䔈͙ի۾̹̯͙࣪իȡ℃ັIV = 5 – 1喛ॕ
݈喌ᄵᒂݼիߏڔݟ㐂᳋͜喌♥ऽᐯ໺̺̯⃤䃟ᒄȡ℃ັVI = 5 + 1, II=1+1
Вⴰ
// LeetCode, Roman to Integer
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
inline int map(const char c) {
switch (c) {
case 'I': return 1;
case 'V': return 5;
case 'X': return 10;
case 'L': return 50;
case 'C': return 100;
case 'D': return 500;
case 'M': return 1000;
default: return 0;
}
}
int romanToInt(const string& s) {
int result = 0;
for (size_t i = 0; i < s.size(); i++) {
if (i > 0 && map(s[i]) > map(s[i - 1])) {
result += (map(s[i]) - 2 * map(s[i - 1]));
} else {

---

74
せ3 』
ႆさ͡
result += map(s[i]);
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• Integer to Roman, 㻰§3.10
3.12
Count and Say
᣾䔟
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2", then "one 1" or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
ܵᲿ
ὐ᠎ȡ
Вⴰ
// LeetCode, Count and Say
// @author 䔍೽(http://weibo.com/lianchengzju)
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
string countAndSay(int n) {
string s("1");
while (--n)
s = getNext(s);
return s;
}
string getNext(const string &s) {
stringstream ss;

---

3.13
Anagrams
75
for (auto i = s.begin(); i != s.end(); ) {
auto j = find_if(i, s.end(), bind1st(not_equal_to<char>(), *i));
ss << distance(i, j) << *i;
i = j;
}
return ss.str();
}
};
Ⱗڢ题Ⱍ
• ᬏ
3.13
Anagrams
᣾䔟
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.
ܵᲿ
Anagram喈఍᪶Ჳ䃼∄喉᭞ᠶគΠႆ⃼䶩ᎾϽ㔻ᓆݟ᫟⮳ࢄ䃼喌℃ັ"dormitory" គΠႆ⃼䶩
Ꮎщइ᜿"dirty room" 喌"tea" щइ᜿"eat"ȡ
఍᪶Ჳ䃼∄᰸̯͙➨◨喚ࢄ䃼䛻⮳ႆ⃼⮳⻼ㆪ঻᪟Ⱍ⇐᰸ᩨइ喌ङ᭞ᩨइεႆ⃼⮳ᣁ݆䶩Ꮎȡఏ
ₓ喌ᄵ܏͙ࢄ䃼ᠸ⚖ႆ⃼䶩ᎾᣁᎾऽ喌㠔ႲЛⰧへ喌݈ႲЛᆍνऻ̯㏳anagrams ȡ
Вⴰ
// LeetCode, Anagrams
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<string> anagrams(vector<string> &strs) {
unordered_map<string, vector<string> > group;
for (const auto &s : strs) {
string key = s;
sort(key.begin(), key.end());
group[key].push_back(s);
}
vector<string> result;
for (auto it = group.cbegin(); it != group.cend(); it++) {
if (it->second.size() > 1)
result.insert(result.end(), it->second.begin(), it->second.end());
}

---

76
せ3 』
ႆさ͡
return result;
}
};
Ⱗڢ题Ⱍ
• ᬏ
3.14
Simplify Path
᣾䔟
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Corner Cases:
• Did you consider the case where path = "/../"? In this case, you should return "/".
• Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
ܵᲿ
ᒷ᰸Ⴭ䭴Цի⮳题Ⱍȡ
Вⴰ
// LeetCode, Simplify Path
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
string simplifyPath(const string& path) {
vector<string> dirs; // ᒂ։ᴷ
for (auto i = path.begin(); i != path.end();) {
++i;
auto j = find(i, path.end(), '/');
auto dir = string(i, j);
if (!dir.empty() && dir != ".") {// ᒂ᰸䔍㐜'///' ᬥ喌dir ͩ⾩
if (dir == "..") {
if (!dirs.empty())
dirs.pop_back();

---

3.15
Length of Last Word
77
} else
dirs.push_back(dir);
}
i = j;
}
stringstream out;
if (dirs.empty()) {
out << "/";
} else {
for (auto dir : dirs)
out << '/' << dir;
}
return out.str();
}
};
Ⱗڢ题Ⱍ
• ᬏ
3.15
Length of Last Word
᣾䔟
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length
of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example, Given s = "Hello World", return 5.
ܵᲿ
㏵㞱Ⴭ⣟题ȡ
⩗STL
// LeetCode, Length of Last Word
// ֦ᜁ喌⩗STL
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int lengthOfLastWord(const string& s) {
auto first = find_if(s.rbegin(), s.rend(), ::isalpha);
auto last = find_if_not(first, s.rend(), ::isalpha);

---

78
せ3 』
ႆさ͡
return distance(first, last);
}
};
䶩Ꮎរ᣾
// LeetCode, Length of Last Word
// 䶩Ꮎរ᣾喌䃟ᒄ⃾͙ word ⮳䪮Ꮥ
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int lengthOfLastWord(const string& s) {
return lengthOfLastWord(s.c_str());
}
private:
int lengthOfLastWord(const char *s) {
int len = 0;
while (*s) {
if (*s++ != ' ')
++len;
else if (*s && *s != ' ')
len = 0;
}
return len;
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

せ4 』
ᴷ঻䭎݆
4.1
ᴷ
4.1.1
Valid Parentheses
᣾䔟
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string is valid.
The brackets must close in the correct order, "()" and "()[]" are all valid but "(]" and "([)]" are
not.
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Valid Parentheses
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
bool isValid (string const& s) {
string left = "([{";
string right = ")]}";
stack<char> stk;
for (auto c : s) {
if (left.find(c) != string::npos) {
stk.push (c);
} else {
if (stk.empty () || stk.top () != left[right.find (c)])
return false;
else
stk.pop ();
}
}
79

---

80
せ4 』
ᴷ঻䭎݆
return stk.empty();
}
};
Ⱗڢ题Ⱍ
• Generate Parentheses, 㻰§10.9
• Longest Valid Parentheses, 㻰§4.1.2
4.1.2
Longest Valid Parentheses
᣾䔟
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-
formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", which has
length = 4.
ܵᲿ
ᬏ
Ү⩗ᴷ
// LeetCode, Longest Valid Parenthese
// Ү⩗ᴷ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int longestValidParentheses(const string& s) {
int max_len = 0, last = -1; // the position of the last ')'
stack<int> lefts;
// keep track of the positions of non-matching '('s
for (int i = 0; i < s.size(); ++i) {
if (s[i] =='(') {
lefts.push(i);
} else {
if (lefts.empty()) {
// no matching left
last = i;
} else {
// find a matching pair
lefts.pop();
if (lefts.empty()) {
max_len = max(max_len, i-last);
} else {
max_len = max(max_len, i-lefts.top());

---

4.1
ᴷ
81
}
}
}
}
return max_len;
}
};
Dynamic Programming, One Pass
// LeetCode, Longest Valid Parenthese
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
// @author ̯ङᲟḝ(http://weibo.com/wjson)
class Solution {
public:
int longestValidParentheses(const string& s) {
vector<int> f(s.size(), 0);
int ret = 0;
for (int i = s.size() - 2; i >= 0; --i) {
int match = i + f[i + 1] + 1;
// case: "((...))"
if (s[i] == '(' && match < s.size() && s[match] == ')') {
f[i] = f[i + 1] + 2;
// if a valid sequence exist afterwards "((...))()"
if (match + 1 < s.size()) f[i] += f[match + 1];
}
ret = max(ret, f[i]);
}
return ret;
}
};
͓䕼រ᣾
// LeetCode, Longest Valid Parenthese
// ͓䕼រ᣾喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
// @author ᰨ卾(http://weibo.com/cpcs)
class Solution {
public:
int longestValidParentheses(const string& s) {
int answer = 0, depth = 0, start = -1;
for (int i = 0; i < s.size(); ++i) {
if (s[i] == '(') {
++depth;
} else {
--depth;
if (depth < 0) {
start = i;
depth = 0;
} else if (depth == 0) {
answer = max(answer, i - start);
}

---

82
せ4 』
ᴷ঻䭎݆
}
}
depth = 0;
start = s.size();
for (int i = s.size() - 1; i >= 0; --i) {
if (s[i] == ')') {
++depth;
} else {
--depth;
if (depth < 0) {
start = i;
depth = 0;
} else if (depth == 0) {
answer = max(answer, start - i);
}
}
}
return answer;
}
};
Ⱗڢ题Ⱍ
• Valid Parentheses, 㻰§4.1.1
• Generate Parentheses, 㻰§10.9
4.1.3
Largest Rectangle in Histogram
᣾䔟
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
భ4-1
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![Leetcode-CPP 第88页插图](../assets/images/Leetcode-CPP_p88_1_ccea9298.png)

---

4.1
ᴷ
83
భ4-2
The largest rectangle is shown in the shaded area, which has area = 10 unit.
For example, Given height = [2,1,5,6,2,3], return 10.
ܵᲿ
クࢄ⮳喌ㆪѫν Container With Most Water(§12.6)喌ᄨ⃾͙ᴠၿ喌ጕढមᆄ喌Ⱓݟ⷟ݟ℃㜙ጠⴝ
⮳喌䃐テ䔈͙ⴘᒑ⮳䲑⼞喌⩗̯͙इ䛾䃟ᒄᰯ๖⮳䲑⼞喌฼ᱱᏕO(n2)喌щ䊴ᬥȡ
ັభ§4-2ᝯ⹩喌Ͻጕݟढำ⤵Ⱓ᫨喌ᒂi = 4 ᬥ喌ᄾνᒂݼᴷ䶥喈ࢢⰣ᫨3喉喌ᄨνⰣ᫨3喌ᬏ䃩ऽ
䲑䔇᭞ݼ䲑⮳Ⱓ᫨喌䘬̼ञ㘬ᓆݟ℃Ⱍݼᴷ䶥ٲ㉏ᰣ倇⮳倇Ꮥε喌ำ⤵ᢸⰣ᫨3喈䃐テϽⰣ᫨3 ݟⰣ
᫨4 ͺ䬣⮳ⴘᒑ⮳䲑⼞喌♥ऽϽᴷ䛻ᑨܩ喉喛ᄨνⰣ᫨2 Ύ᭞ັₓ喛Ⱓݟ⷟ݟ℃Ⱓ᫨4 ᰣⴝ⮳Ⱓ᫨1ȡ
䔈ᅠᘾঢⱯ喌ञД㐣៓̯͙䕁෍⮳ᴷ喌⃾⁐℃䒲ᴷ䶥̽ᒂݼٲ㉏ȡັ᳋ᒂݼٲ㉏๖νᴷ䶥ٲ㉏喌
݈ڔᴷ喌ॕ݈षᎥ⣟᰸ᴷ喌Ⱓ㜢ᴷ䶥ٲ㉏ᄾνᒂݼٲ㉏ȡ㐂ᅭᬥڔᴷٲ㉏0喌䛼฼षᎥ̯⁐ȡ
Вⴰ
// LeetCode, Largest Rectangle in Histogram
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int largestRectangleArea(vector<int> &height) {
stack<int> s;
height.push_back(0);
int result = 0;
for (int i = 0; i < height.size(); ) {
if (s.empty() || height[i] > height[s.top()])
s.push(i++);
else {
int tmp = s.top();
s.pop();
result = max(result,
height[tmp] * (s.empty() ? i : i - s.top() - 1));
}
}
return result;

![Leetcode-CPP 第89页插图](../assets/images/Leetcode-CPP_p89_1_b056999d.png)

---

84
せ4 』
ᴷ঻䭎݆
}
};
Ⱗڢ题Ⱍ
• Trapping Rain Water, 㻰§2.1.15
• Container With Most Water, 㻰§12.6
4.1.4
Evaluate Reverse Polish Notation
᣾䔟
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Some examples:
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
ܵᲿ
ᬏ
䕁ᒁ❷
// LeetCode, Evaluate Reverse Polish Notation
// 䕁ᒁ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
int evalRPN(vector<string> &tokens) {
int x, y;
auto token = tokens.back();
tokens.pop_back();
if (is_operator(token))
{
y = evalRPN(tokens);
x = evalRPN(tokens);
if (token[0] == '+')
x += y;
else if (token[0] == '-')
x -= y;
else if (token[0] == '*')
x *= y;
else
x /= y;
} else
{
size_t i;
x = stoi(token, &i);
}
return x;
}
private:
bool is_operator(const string &op) {
return op.size() == 1 && string("+-*/").find(op) != string::npos;
}
};

---

4.2
䭎݆
85
䔜В❷
// LeetCode, Max Points on a Line
// 䔜В喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
int evalRPN(vector<string> &tokens) {
stack<string> s;
for (auto token : tokens) {
if (!is_operator(token)) {
s.push(token);
} else {
int y = stoi(s.top());
s.pop();
int x = stoi(s.top());
s.pop();
if (token[0] == '+')
x += y;
else if (token[0] == '-')
x -= y;
else if (token[0] == '*')
x *= y;
else
x /= y;
s.push(to_string(x));
}
}
return stoi(s.top());
}
private:
bool is_operator(const string &op) {
return op.size() == 1 && string("+-*/").find(op) != string::npos;
}
};
Ⱗڢ题Ⱍ
• ᬏ
4.2
䭎݆

---

せ5 』
ᵀ
LeetCode ̹λࣸᵀ⮳㞱◨჉͸ັ̺喚
// ᵀ⮳㞱◨
struct TreeNode {
int val;
TreeNode *left;
TreeNode *right;
TreeNode(int x) : val(x), left(nullptr), right(nullptr) { }
};
5.1
λࣸᵀ⮳䕼ࢵ
ᵀ⮳䕼ࢵ᰸͓ㆪ喚⌠Ꮥчٷ䕼ࢵ঻წᏕчٷ䕼ࢵȡ⌠Ꮥчٷ䕼ࢵࣷञ͓ܵͩ⻼喚ٷᵨ喈⁐Ꮎ喉䕼ࢵ঻
ऽᵨ喈⁐Ꮎ喉䕼ࢵȡ
ᵀ⮳ٷᵨ䕼ࢵ᭞喚ٷ䃮䬝ᵀ⮳ᵨ㐂◨喌♥ऽӌ⁐ٷᵨ䕼ࢵᵨ⮳ळḤၿᵀȡᵀ⮳ٷ䌎䕼ࢵ⮳㐂᳋
̽ᄨᏃλࣸᵀ喈႘ၿٳᑎ㶗⹩∄喉⮳ٷᎾ䕼ࢵ⮳㐂᳋Ⱗऻȡ
ᵀ⮳ऽᵨ䕼ࢵ᭞喚ٷӌ⁐ऽᵨ䕼ࢵᵀᵨ⮳ळḤၿᵀ喌♥ऽ䃮䬝ᵨ㐂◨ȡᵀ⮳ऽ䌎䕼ࢵ⮳㐂᳋̽
ᄨᏃλࣸᵀ⮳͜Ꮎ䕼ࢵ⮳㐂᳋Ⱗऻȡ
λࣸᵀ⮳ٷᵨ䕼ࢵ᰸喚ٷᎾ䕼ࢵ(root->left->right)喌root->right->left喛ऽᵨ䕼ࢵ᰸喚ऽᎾ䕼ࢵ(left-
>right->root)喌right->left->root喛λࣸᵀ䔇᰸͙̯㝛⮳ᵀ⇐᰸⮳䕼ࢵ⁐Ꮎ喌͜Ꮎ䕼ࢵ(left->root->right)ȡ
5.1.1
Binary Tree Preorder Traversal
᣾䔟
Given a binary tree, return the preorder traversal of its nodes’ values.
For example: Given binary tree {1,#,2,3},
1
\
2
/
3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?
86

---

5.1
λࣸᵀ⮳䕼ࢵ
87
ܵᲿ
⩗ᴷᝅ㔴Morris 䕼ࢵȡ
ᴷ
// LeetCode, Binary Tree Preorder Traversal
// Ү⩗ᴷ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<int> preorderTraversal(TreeNode *root) {
vector<int> result;
stack<const TreeNode *> s;
if (root != nullptr) s.push(root);
while (!s.empty()) {
const TreeNode *p = s.top();
s.pop();
result.push_back(p->val);
if (p->right != nullptr) s.push(p->right);
if (p->left != nullptr) s.push(p->left);
}
return result;
}
};
Morris ٷᎾ䕼ࢵ
// LeetCode, Binary Tree Preorder Traversal
// Morris ٷᎾ䕼ࢵ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> preorderTraversal(TreeNode *root) {
vector<int> result;
TreeNode *cur = root, *prev = nullptr;
while (cur != nullptr) {
if (cur->left == nullptr) {
result.push_back(cur->val);
prev = cur; /* cur ݉݉㷚䃮䬝䓶*/
cur = cur->right;
} else {
/* ᴔឭݼ侠*/
TreeNode *node = cur->left;
while (node->right != nullptr && node->right != cur)
node = node->right;
if (node->right == nullptr) { /* 䔇⇐㏮㉑ࡅ喌݈ᐩ⿺㏮㉑*/
result.push_back(cur->val); /* ϴ䔈̯㵻⮳Ѽ㒝̽͜Ꮎ̼ऻ*/
node->right = cur;
prev = cur; /* cur ݉݉㷚䃮䬝䓶*/

---

88
せ5 』
ᵀ
cur = cur->left;
} else {
/* ጡ㏾㏮㉑ࡅ喌݈ݏ䮓㏮㉑
*/
node->right = nullptr;
/* prev = cur; ̼㘬᰸䔈औ喌cur ጡ㏾㷚䃮䬝*/
cur = cur->right;
}
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• Binary Tree Inorder Traversal喌㻰§5.1.2
• Binary Tree Postorder Traversal喌㻰§5.1.3
• Recover Binary Search Tree喌㻰§5.1.7
5.1.2
Binary Tree Inorder Traversal
᣾䔟
Given a binary tree, return the inorder traversal of its nodes’ values.
For example: Given binary tree {1,#,2,3},
1
\
2
/
3
return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
ܵᲿ
⩗ᴷᝅ㔴Morris 䕼ࢵȡ
ᴷ
// LeetCode, Binary Tree Inorder Traversal
// Ү⩗ᴷ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<int> inorderTraversal(TreeNode *root) {
vector<int> result;
stack<const TreeNode *> s;
const TreeNode *p = root;

---

5.1
λࣸᵀ⮳䕼ࢵ
89
while (!s.empty() || p != nullptr) {
if (p != nullptr) {
s.push(p);
p = p->left;
} else {
p = s.top();
s.pop();
result.push_back(p->val);
p = p->right;
}
}
return result;
}
};
Morris ͜Ꮎ䕼ࢵ
// LeetCode, Binary Tree Inorder Traversal
// Morris ͜Ꮎ䕼ࢵ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> inorderTraversal(TreeNode *root) {
vector<int> result;
TreeNode *cur = root, *prev = nullptr;
while (cur != nullptr) {
if (cur->left == nullptr) {
result.push_back(cur->val);
prev = cur;
cur = cur->right;
} else {
/* ᴔឭݼ侠*/
TreeNode *node = cur->left;
while (node->right != nullptr && node->right != cur)
node = node->right;
if (node->right == nullptr) { /* 䔇⇐㏮㉑ࡅ喌݈ᐩ⿺㏮㉑*/
node->right = cur;
/* prev = cur; ̼㘬᰸䔈औ喌cur 䔇⇐᰸㷚䃮䬝*/
cur = cur->left;
} else {
/* ጡ㏾㏮㉑ࡅ喌݈䃮䬝㞱◨喌Ꭵݏ䮓㏮㉑
*/
result.push_back(cur->val);
node->right = nullptr;
prev = cur;
cur = cur->right;
}
}
}
return result;
}
};

---

90
せ5 』
ᵀ
Ⱗڢ题Ⱍ
• Binary Tree Preorder Traversal喌㻰§5.1.1
• Binary Tree Postorder Traversal喌㻰§5.1.3
• Recover Binary Search Tree喌㻰§5.1.7
5.1.3
Binary Tree Postorder Traversal
᣾䔟
Given a binary tree, return the postorder traversal of its nodes’ values.
For example: Given binary tree {1,#,2,3},
1
\
2
/
3
return [3,2,1].
Note: Recursive solution is trivial, could you do it iteratively?
ܵᲿ
⩗ᴷᝅ㔴Morris 䕼ࢵȡ
ᴷ
// LeetCode, Binary Tree Postorder Traversal
// Ү⩗ᴷ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<int> postorderTraversal(TreeNode *root) {
vector<int> result;
stack<const TreeNode *> s;
/* p喌ₒ౗䃮䬝⮳㐂◨喌q喌݉݉䃮䬝䓶⮳㐂◨*/
const TreeNode *p = root, *q = nullptr;
do {
while (p != nullptr) { /* ᒯጕ̺䊟*/
s.push(p);
p = p->left;
}
q = nullptr;
while (!s.empty()) {
p = s.top();
s.pop();
/* ढ႘ၿ̼ႇ౗ᝅጡ㷚䃮䬝喌䃮䬝ͺ */
if (p->right == q) {

---

5.1
λࣸᵀ⮳䕼ࢵ
91
result.push_back(p->val);
q = p; /* Ԍႇ݉䃮䬝䓶⮳㐂◨*/
} else {
/* ᒂݼ㐂◨̼㘬䃮䬝喌䰯せλ⁐䔊ᴷ*/
s.push(p);
/* ٷำ⤵ढၿᵀ*/
p = p->right;
break;
}
}
} while (!s.empty());
return result;
}
};
Morris ऽᎾ䕼ࢵ
// LeetCode, Binary Tree Postorder Traversal
// Morris ऽᎾ䕼ࢵ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> postorderTraversal(TreeNode *root) {
vector<int> result;
TreeNode dummy(-1);
TreeNode *cur, *prev = nullptr;
std::function < void(const TreeNode*)> visit =
[&result](const TreeNode *node){
result.push_back(node->val);
};
dummy.left = root;
cur = &dummy;
while (cur != nullptr) {
if (cur->left == nullptr) {
prev = cur; /* ᓴ䶪㺰᰸*/
cur = cur->right;
} else {
TreeNode *node = cur->left;
while (node->right != nullptr && node->right != cur)
node = node->right;
if (node->right == nullptr) { /* 䔇⇐㏮㉑ࡅ喌݈ᐩ⿺㏮㉑*/
node->right = cur;
prev = cur; /* ᓴ䶪㺰᰸*/
cur = cur->left;
} else { /* ጡ㏾㏮㉑ࡅ喌݈䃮䬝㞱◨喌Ꭵݏ䮓㏮㉑
*/
visit_reverse(cur->left, prev, visit);
prev->right = nullptr;
prev = cur; /* ᓴ䶪㺰᰸*/
cur = cur->right;
}
}

---

92
せ5 』
ᵀ
}
return result;
}
private:
// 䔵䒛䌞ᒳ
static void reverse(TreeNode *from, TreeNode *to) {
TreeNode *x = from, *y = from->right, *z;
if (from == to) return;
while (x != to) {
z = y->right;
y->right = x;
x = y;
y = z;
}
}
// 䃮䬝䔵䒛ऽ⮳䌞ᒳ̹⮳ᝯ᰸㐂◨
static void visit_reverse(TreeNode* from, TreeNode *to,
std::function< void(const TreeNode*) >& visit) {
TreeNode *p = to;
reverse(from, to);
while (true) {
visit(p);
if (p == from)
break;
p = p->right;
}
reverse(to, from);
}
};
Ⱗڢ题Ⱍ
• Binary Tree Preorder Traversal喌㻰§5.1.1
• Binary Tree Inorder Traversal喌㻰§5.1.2
• Recover Binary Search Tree喌㻰§5.1.7
5.1.4
Binary Tree Level Order Traversal
᣾䔟
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by
level).
For example: Given binary tree {3,9,20,#,#,15,7},

---

5.1
λࣸᵀ⮳䕼ࢵ
93
3
/ \
9
20
/
\
15
7
return its level order traversal as:
[
[3],
[9,20],
[15,7]
]
ܵᲿ
ᬏ
䕁ᒁ❷
// LeetCode, Binary Tree Level Order Traversal
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > levelOrder(TreeNode *root) {
vector<vector<int>> result;
traverse(root, 1, result);
return result;
}
void traverse(TreeNode *root, size_t level, vector<vector<int>> &result) {
if (!root) return;
if (level > result.size())
result.push_back(vector<int>());
result[level-1].push_back(root->val);
traverse(root->left, level+1, result);
traverse(root->right, level+1, result);
}
};
䔜В❷
// LeetCode, Binary Tree Level Order Traversal
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > levelOrder(TreeNode *root) {
vector<vector<int> > result;
queue<TreeNode*> current, next;

---

94
せ5 』
ᵀ
if(root == nullptr) {
return result;
} else {
current.push(root);
}
while (!current.empty()) {
vector<int> level; // elments in one level
while (!current.empty()) {
TreeNode* node = current.front();
current.pop();
level.push_back(node->val);
if (node->left != nullptr) next.push(node->left);
if (node->right != nullptr) next.push(node->right);
}
result.push_back(level);
swap(next, current);
}
return result;
}
};
Ⱗڢ题Ⱍ
• Binary Tree Level Order Traversal II喌㻰§5.1.5
• Binary Tree Zigzag Level Order Traversal喌㻰§5.1.6
5.1.5
Binary Tree Level Order Traversal II
᣾䔟
Given a binary tree, return the bottom-up level order traversal of its nodes’ values. (ie, from left to right,
level by level from leaf to root).
For example: Given binary tree {3,9,20,#,#,15,7},
3
/ \
9
20
/
\
15
7
return its bottom-up level order traversal as:
[
[15,7]
[9,20],
[3],
]

---

5.1
λࣸᵀ⮳䕼ࢵ
95
ܵᲿ
౗̹̯题喈㻰§5.1.4喉⮳ഩⵯ̹喌reverse() ̯̺ࢢञȡ
䕁ᒁ❷
// LeetCode, Binary Tree Level Order Traversal II
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > levelOrderBottom(TreeNode *root) {
vector<vector<int>> result;
traverse(root, 1, result);
std::reverse(result.begin(), result.end()); // ℃̹̯题้ₓ̯㵻
return result;
}
void traverse(TreeNode *root, size_t level, vector<vector<int>> &result) {
if (!root) return;
if (level > result.size())
result.push_back(vector<int>());
result[level-1].push_back(root->val);
traverse(root->left, level+1, result);
traverse(root->right, level+1, result);
}
};
䔜В❷
// LeetCode, Binary Tree Level Order Traversal II
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > levelOrderBottom(TreeNode *root) {
vector<vector<int> > result;
if(root == nullptr) return result;
queue<TreeNode*> current, next;
vector<int> level; // elments in level level
current.push(root);
while (!current.empty()) {
while (!current.empty()) {
TreeNode* node = current.front();
current.pop();
level.push_back(node->val);
if (node->left != nullptr) next.push(node->left);
if (node->right != nullptr) next.push(node->right);
}
result.push_back(level);

---

96
せ5 』
ᵀ
level.clear();
swap(next, current);
}
reverse(result.begin(), result.end()); // ℃̹̯题้ₓ̯㵻
return result;
}
};
Ⱗڢ题Ⱍ
• Binary Tree Level Order Traversal喌㻰§5.1.4
• Binary Tree Zigzag Level Order Traversal喌㻰§5.1.6
5.1.6
Binary Tree Zigzag Level Order Traversal
᣾䔟
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right,
then right to left for the next level and alternate between).
For example: Given binary tree 3,9,20,#,#,15,7,
3
/ \
9
20
/
\
15
7
return its zigzag level order traversal as:
[
[3],
[20,9],
[15,7]
]
ܵᲿ
ᎮᏕчٷ䕼ࢵ喌⩗̯͙ bool 䃟ᒄ᭞Ͻጕݟढ䔇᭞Ͻढݟጕ喌⃾̯ᅱ㐂᲎ᅠ㔪䒛̯̺ȡ
䕁ᒁ❷
// LeetCode, Binary Tree Zigzag Level Order Traversal
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
vector<vector<int>> result;
traverse(root, 1, result, true);
return result;

---

5.1
λࣸᵀ⮳䕼ࢵ
97
}
void traverse(TreeNode *root, size_t level, vector<vector<int>> &result,
bool left_to_right) {
if (!root) return;
if (level > result.size())
result.push_back(vector<int>());
if (left_to_right)
result[level-1].push_back(root->val);
else
result[level-1].insert(result[level-1].begin(), root->val);
traverse(root->left, level+1, result, !left_to_right);
traverse(root->right, level+1, result, !left_to_right);
}
};
䔜В❷
//LeetCode, Binary Tree Zigzag Level Order Traversal
//ᎮᏕчٷ䕼ࢵ喌⩗̯͙ bool 䃟ᒄ᭞Ͻጕݟढ䔇᭞Ͻढݟጕ喌⃾̯ᅱ㐂᲎ᅠ㔪䒛̯̺ȡ
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
vector<vector<int> > result;
queue<TreeNode*> current, next;
bool left_to_right = true;
if(root == nullptr) {
return result;
} else {
current.push(root);
}
while (!current.empty()) {
vector<int> level; // elments in one level
while (!current.empty()) {
TreeNode* node = current.front();
current.pop();
level.push_back(node->val);
if (node->left != nullptr) next.push(node->left);
if (node->right != nullptr) next.push(node->right);
}
if (!left_to_right) reverse(level.begin(), level.end());
result.push_back(level);
left_to_right = !left_to_right;
swap(next, current);
}
return result;
}

---

98
せ5 』
ᵀ
};
Ⱗڢ题Ⱍ
• Binary Tree Level Order Traversal喌㻰§5.1.4
• Binary Tree Level Order Traversal II喌㻰§5.1.5
5.1.7
Recover Binary Search Tree
᣾䔟
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
ܵᲿ
O(n) ⾩䬣⮳解∄᭞喌ᐯ̯͙ᠶ䦷᪟㏳喌͜Ꮎ䕼ࢵ喌ᄵ㞱◨ᠶ䦷ӌ⁐ႇᩭݟ᪟㏳䛻喌♥ऽᄪឭ͓
ำ䔵ी⮳Ѽ㒝喌ٷϽݼᒯऽឭせ̯͙䔵Ꮎ⮳Ѽ㒝喌♥ऽϽऽᒯݼឭせλ͙䔵Ꮎ⮳Ѽ㒝喌ϓᢑ䔈͓͙
ᠶ䦷⮳իȡ
͜Ꮎ䕼ࢵ̯㝛䰯㺰⩗ݟᴷ喌⾩䬣Ύ᭞O(n) ⮳喌ັ҄᝼㘬̼Ү⩗ᴷ喟Morris ͜Ꮎ䕼ࢵȡ
Вⴰ
// LeetCode, Recover Binary Search Tree
// Morris ͜Ꮎ䕼ࢵ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void recoverTree(TreeNode* root) {
pair<TreeNode*, TreeNode*> broken;
TreeNode* prev = nullptr;
TreeNode* cur = root;
while (cur != nullptr) {
if (cur->left == nullptr) {
detect(broken, prev, cur);
prev = cur;
cur = cur->right;
} else {
auto node = cur->left;
while (node->right != nullptr && node->right != cur)
node = node->right;
if (node->right == nullptr) {
node->right = cur;
//prev = cur; ̼㘬᰸䔈औ喁ఏͩ cur 䔇⇐᰸㷚䃮䬝

---

5.1
λࣸᵀ⮳䕼ࢵ
99
cur = cur->left;
} else {
detect(broken, prev, cur);
node->right = nullptr;
prev = cur;
cur = cur->right;
}
}
}
swap(broken.first->val, broken.second->val);
}
void detect(pair<TreeNode*, TreeNode*>& broken, TreeNode* prev,
TreeNode* current) {
if (prev != nullptr && prev->val > current->val) {
if (broken.first == nullptr) {
broken.first = prev;
} //̼㘬⩗else喌Һັ{0,1}喌щᄫ㜣ᰯऽswap ᬥsecond ͩ nullptr喌
//щ Runtime Error
broken.second = current;
}
}
};
Ⱗڢ题Ⱍ
• Binary Tree Inorder Traversal喌㻰§5.1.2
5.1.8
Same Tree
᣾䔟
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
ܵᲿ
ᬏ
䕁ᒁ❷
䕁ᒁ❷
// LeetCode, Same Tree
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
bool isSameTree(TreeNode *p, TreeNode *q) {

---

100
せ5 』
ᵀ
if (!p && !q) return true;
// ㏷ₑᲐХ
if (!p || !q) return false;
// ޙ᳌
return p->val == q->val
// ̸᫨षᎥ
&& isSameTree(p->left, q->left)
&& isSameTree(p->right, q->right);
}
};
䔜В❷
// LeetCode, Same Tree
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
bool isSameTree(TreeNode *p, TreeNode *q) {
stack<TreeNode*> s;
s.push(p);
s.push(q);
while(!s.empty()) {
p = s.top(); s.pop();
q = s.top(); s.pop();
if (!p && !q) continue;
if (!p || !q) return false;
if (p->val != q->val) return false;
s.push(p->left);
s.push(q->left);
s.push(p->right);
s.push(q->right);
}
return true;
}
};
Ⱗڢ题Ⱍ
• Symmetric Tree喌㻰§5.1.9
5.1.9
Symmetric Tree
᣾䔟
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

---

5.1
λࣸᵀ⮳䕼ࢵ
101
ܵᲿ
ᬏ
䕁ᒁ❷
// LeetCode, Symmetric Tree
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
bool isSymmetric(TreeNode *root) {
if (root == nullptr) return true;
return isSymmetric(root->left, root->right);
}
bool isSymmetric(TreeNode *p, TreeNode *q) {
if (p == nullptr && q == nullptr) return true;
// ㏷ₑᲐХ
if (p == nullptr || q == nullptr) return false;
// ㏷ₑᲐХ
return p->val == q->val
// ̸᫨षᎥ
&& isSymmetric(p->left, q->right)
&& isSymmetric(p->right, q->left);
}
};
䔜В❷
// LeetCode, Symmetric Tree
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
bool isSymmetric (TreeNode* root) {
if (!root) return true;
stack<TreeNode*> s;
s.push(root->left);
s.push(root->right);
while (!s.empty ()) {
auto p = s.top (); s.pop();
auto q = s.top (); s.pop();
if (!p && !q) continue;
if (!p || !q) return false;
if (p->val != q->val) return false;
s.push(p->left);
s.push(q->right);
s.push(p->right);
s.push(q->left);
}
return true;

---

102
せ5 』
ᵀ
}
};
Ⱗڢ题Ⱍ
• Same Tree喌㻰§5.1.8
5.1.10
Balanced Binary Tree
᣾䔟
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
subtrees of every node never differ by more than 1.
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Balanced Binary Tree
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
bool isBalanced (TreeNode* root) {
return balancedHeight (root) >= 0;
}
/**
* Returns the height of `root` if `root` is a balanced tree,
* otherwise, returns `-1`.
*/
int balancedHeight (TreeNode* root) {
if (root == nullptr) return 0;
// ㏷ₑᲐХ
int left = balancedHeight (root->left);
int right = balancedHeight (root->right);
if (left < 0 || right < 0 || abs(left - right) > 1) return -1;
// ޙ᳌
return max(left, right) + 1; // ̸᫨षᎥ
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

5.1
λࣸᵀ⮳䕼ࢵ
103
5.1.11
Flatten Binary Tree to Linked List
᣾䔟
Given a binary tree, flatten it to a linked list in-place.
For example, Given
1
/ \
2
5
/ \
\
3
4
6
The flattened tree should look like:
1
\
2
\
3
\
4
\
5
\
6
ܵᲿ
ᬏ
䕁ᒁ❷1
// LeetCode, Flatten Binary Tree to Linked List
// 䕁ᒁ❷1喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
void flatten(TreeNode *root) {
if (root == nullptr) return;
// ㏷ₑᲐХ
flatten(root->left);
flatten(root->right);
if (nullptr == root->left) return;
// ̸᫨षᎥ喌ᄵጕၿᵀᝯᒑ᜿⮳䨭㶗ᤁڔݟroot ঻root->right ͺ䬣
TreeNode *p = root->left;
while(p->right) p = p->right; //ᄪឭጕ䨭㶗ᰯऽ̯͙㞱◨
p->right = root->right;
root->right = root->left;
root->left = nullptr;
}
};

---

104
せ5 』
ᵀ
䕁ᒁ❷2
// LeetCode, Flatten Binary Tree to Linked List
// 䕁ᒁ❷2
// @author ⢺䶩䓭(http://weibo.com/u/1234984145)
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
void flatten(TreeNode *root) {
flatten(root, NULL);
}
private:
// ឹroot ᝯВ㶗ᵀइ᜿䨭㶗ऽ喌tail 䌎౗䄔䨭㶗ऽ䲑
TreeNode *flatten(TreeNode *root, TreeNode *tail) {
if (NULL == root) return tail;
root->right = flatten(root->left, flatten(root->right, tail));
root->left = NULL;
return root;
}
};
䔜В❷
// LeetCode, Flatten Binary Tree to Linked List
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
void flatten(TreeNode* root) {
if (root == nullptr) return;
stack<TreeNode*> s;
s.push(root);
while (!s.empty()) {
auto p = s.top();
s.pop();
if (p->right)
s.push(p->right);
if (p->left)
s.push(p->left);
p->left = nullptr;
if (!s.empty())
p->right = s.top();
}
}
};

---

5.1
λࣸᵀ⮳䕼ࢵ
105
Ⱗڢ题Ⱍ
• ᬏ
5.1.12
Populating Next Right Pointers in Each Node II
᣾䔟
Follow up for problem ”Populating Next Right Pointers in Each Node”.
What if the given tree could be any binary tree? Would your previous solution still work?
Note: You may only use constant extra space.
For example, Given the following binary tree,
1
/
\
2
3
/ \
\
4
5
7
After calling your function, the tree should look like:
1 -> NULL
/
\
2 -> 3 -> NULL
/ \
\
4-> 5 -> 7 -> NULL
ܵᲿ
㺰ำ⤵̯͙㞱◨喌ञ㘬䰯㺰ᰯढ䓨⮳ٳᑎ㞱◨喌仅ٷᘢݟ⩗Ꭾ᥋ȡѵᎮ᥋̼᭞፧᪟⾩䬣⮳喌ᱛ题
㺰ⅱ፧᪟⾩䬣ȡ
∗ᘾ喌䔈题⮳Вⴰ࣎ᄰ̼ߗ喌ΎञД解ۢ Populating Next Right Pointers in Each Node I.
䕁ᒁ❷
// LeetCode, Populating Next Right Pointers in Each Node II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void connect(TreeLinkNode *root) {
if (root == nullptr) return;
TreeLinkNode dummy(-1);
for (TreeLinkNode *curr = root, *prev = &dummy;
curr; curr = curr->next) {
if (curr->left != nullptr){
prev->next = curr->left;
prev = prev->next;
}
if (curr->right != nullptr){

---

106
せ5 』
ᵀ
prev->next = curr->right;
prev = prev->next;
}
}
connect(dummy.next);
}
};
䔜В❷
// LeetCode, Populating Next Right Pointers in Each Node II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void connect(TreeLinkNode *root) {
while (root) {
TreeLinkNode * next = nullptr; // the first node of next level
TreeLinkNode * prev = nullptr; // previous node on the same level
for (; root; root = root->next) {
if (!next) next = root->left ? root->left : root->right;
if (root->left) {
if (prev) prev->next = root->left;
prev = root->left;
}
if (root->right) {
if (prev) prev->next = root->right;
prev = root->right;
}
}
root = next; // turn to next level
}
}
};
Ⱗڢ题Ⱍ
• Populating Next Right Pointers in Each Node喌㻰§5.4.6
5.2
λࣸᵀ⮳Ჳᐩ
5.2.1
Construct Binary Tree from Preorder and Inorder Traversal
᣾䔟
Given preorder and inorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.

---

5.2
λࣸᵀ⮳Ჳᐩ
107
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Construct Binary Tree from Preorder and Inorder Traversal
// 䕁ᒁ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(\logn)
class Solution {
public:
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
return buildTree(begin(preorder), end(preorder),
begin(inorder), end(inorder));
}
template<typename InputIterator>
TreeNode* buildTree(InputIterator pre_first, InputIterator pre_last,
InputIterator in_first, InputIterator in_last) {
if (pre_first == pre_last) return nullptr;
if (in_first == in_last) return nullptr;
auto root = new TreeNode(*pre_first);
auto inRootPos = find(in_first, in_last, *pre_first);
auto leftSize = distance(in_first, inRootPos);
root->left = buildTree(next(pre_first), next(pre_first,
leftSize + 1), in_first, next(in_first, leftSize));
root->right = buildTree(next(pre_first, leftSize + 1), pre_last,
next(inRootPos), in_last);
return root;
}
};
Ⱗڢ题Ⱍ
• Construct Binary Tree from Inorder and Postorder Traversal喌㻰§5.2.2
5.2.2
Construct Binary Tree from Inorder and Postorder Traversal
᣾䔟
Given inorder and postorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.
ܵᲿ
ᬏ

---

108
せ5 』
ᵀ
Вⴰ
// LeetCode, Construct Binary Tree from Inorder and Postorder Traversal
// 䕁ᒁ喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(\logn)
class Solution {
public:
TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
return buildTree(begin(inorder), end(inorder),
begin(postorder), end(postorder));
}
template<typename BidiIt>
TreeNode* buildTree(BidiIt in_first, BidiIt in_last,
BidiIt post_first, BidiIt post_last) {
if (in_first ==in_last) return nullptr;
if (post_first == post_last) return nullptr;
const auto val = *prev(post_last);
TreeNode* root = new TreeNode(val);
auto in_root_pos = find(in_first, in_last, val);
auto left_size = distance(in_first, in_root_pos);
auto post_left_last = next(post_first, left_size);
root->left = buildTree(in_first, in_root_pos, post_first, post_left_last);
root->right = buildTree(next(in_root_pos), in_last, post_left_last,
prev(post_last));
return root;
}
};
Ⱗڢ题Ⱍ
• Construct Binary Tree from Preorder and Inorder Traversal喌㻰§5.2.1
5.3
λࣸᴔឭᵀ
5.3.1
Unique Binary Search Trees
᣾䔟
Given n, how many structurally unique BST’s (binary search trees) that store values 1...n?
For example, Given n = 3, there are a total of 5 unique BST’s.
1
3
3
2
1
\
/
/
/ \
\
3
2
1
1
3
2
/
/
\
\
2
1
2
3

---

5.3
λࣸᴔឭᵀ
109
ܵᲿ
ັ᳋ឹ̹Һ⮳䶩Ꮎᩨ̯̺喌ᅠञДⰺܩ㻳ᒺεȡ
1
1
2
3
3
\
\
/ \
/
/
3
2
1
3
2
1
/
\
/
\
2
3
1
2
℃ັ喌Д 1 ͩᵨ⮳ᵀ⮳͙᪟喌へνጕၿᵀ⮳͙᪟·Дढၿᵀ⮳͙᪟喌ጕၿᵀ᭞0 ͙ٲ㉏⮳ᵀ喌ढ
ၿᵀ᭞2 ͙ٲ㉏⮳ᵀȡД 2 ͩᵨ⮳ᵀ⮳͙᪟喌へνጕၿᵀ⮳͙᪟·Дढၿᵀ⮳͙᪟喌ጕၿᵀ᭞1 ͙
ٲ㉏⮳ᵀ喌ढၿᵀΎ᭞1 ͙ٲ㉏⮳ᵀȡӌₓㆪᣗȡ
ᒂ᪟㏳ͩ 1, 2, 3, ..., n ᬥ喌ഩνД̺݈࣎⮳Ჳᐩ⮳BST ᵀڦ᰸ਫ਼̯ᕖ喚Д i ͩᵨ㞱◨⮳ᵀ喌ڥጕ
ၿᵀ⩠[1, i-1] Ჳ᜿喌ڥढၿᵀ⩠[i+1, n] Ჳ᜿ȡ
჉͸ f(i) ͩД [1, i] 㘬ϖ⩎⮳Unique Binary Search Tree ⮳᪟Ⱍ喌݈
ັ᳋᪟㏳ͩ⾩喌ℚᬏ⫀䬝喌ङ᰸̯⻼BST喌ࢢ⾩ᵀ喌f(0) = 1ȡ
ັ᳋᪟㏳ϴ᰸̯͙ٲ㉏1喌ङ᰸̯⻼BST喌ࢄ͙㞱◨喌f(1) = 1ȡ
ັ᳋᪟㏳᰸͓͙ٲ㉏1,2喌䗒ͷ᰸ັ̺͓⻼ञ㘬
1
2
\
/
2
1
f(2)
=
f(0) ∗f(1) 喌1 ͩᵨ⮳ᗴۤ
+
f(1) ∗f(0) 喌2 ͩᵨ⮳ᗴۤ
ڼⰺ̯ⰺ3 ͙ٲ㉏⮳᪟㏳喌ञДऀ⣟BST ⮳अի᫨ᐾັ̺喚
f(3)
=
f(0) ∗f(2) 喌1 ͩᵨ⮳ᗴۤ
+
f(1) ∗f(1) 喌2 ͩᵨ⮳ᗴۤ
+
f(2) ∗f(0) 喌3 ͩᵨ⮳ᗴۤ
ᝯД喌⩠ₓ㻱ᄎ喌ञДᓆܩf ⮳䕁ᣗڛᐾͩ
f(i) =
i
∑
k=1
f(k −1) × f(i −k)
㜢ₓ喌䬝题݁ᒁ̯ͩ㐣ߗᔰ㻳݁ȡ
Вⴰ
// LeetCode, Unique Binary Search Trees
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {

---

110
せ5 』
ᵀ
public:
int numTrees(int n) {
vector<int> f(n + 1, 0);
f[0] = 1;
f[1] = 1;
for (int i = 2; i <= n; ++i) {
for (int k = 1; k <= i; ++k)
f[i] += f[k-1] * f[i - k];
}
return f[n];
}
};
Ⱗڢ题Ⱍ
• Unique Binary Search Trees II喌㻰§5.3.2
5.3.2
Unique Binary Search Trees II
᣾䔟
Given n, generate all structurally unique BST’s (binary search trees) that store values 1...n.
For example, Given n = 3, your program should return all 5 unique BST’s shown below.
1
3
3
2
1
\
/
/
/ \
\
3
2
1
1
3
2
/
/
\
\
2
1
2
3
ܵᲿ
㻰ݼ䲑̯题ȡ
Вⴰ
// LeetCode, Unique Binary Search Trees II
// ᬥ䬣฼ᱱᏕTODO喌⾩䬣฼ᱱᏕTODO
class Solution {
public:
vector<TreeNode *> generateTrees(int n) {
if (n == 0) return generate(1, 0);
return generate(1, n);
}
private:
vector<TreeNode *> generate(int start, int end) {
vector<TreeNode*> subTree;
if (start > end) {

---

5.3
λࣸᴔឭᵀ
111
subTree.push_back(nullptr);
return subTree;
}
for (int k = start; k <= end; k++) {
vector<TreeNode*> leftSubs = generate(start, k - 1);
vector<TreeNode*> rightSubs = generate(k + 1, end);
for (auto i : leftSubs) {
for (auto j : rightSubs) {
TreeNode *node = new TreeNode(k);
node->left = i;
node->right = j;
subTree.push_back(node);
}
}
}
return subTree;
}
};
Ⱗڢ题Ⱍ
• Unique Binary Search Trees喌㻰§5.3.1
5.3.3
Validate Binary Search Tree
᣾䔟
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.
ܵᲿ
Вⴰ
// LeetCode, Validate Binary Search Tree
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(\logn)
class Solution {
public:
bool isValidBST(TreeNode* root) {
return isValidBST(root, INT_MIN, INT_MAX);
}
bool isValidBST(TreeNode* root, int lower, int upper) {
if (root == nullptr) return true;

---

112
せ5 』
ᵀ
return root->val > lower && root->val < upper
&& isValidBST(root->left, lower, root->val)
&& isValidBST(root->right, root->val, upper);
}
};
Ⱗڢ题Ⱍ
• Validate Binary Search Tree喌㻰§5.3.3
5.3.4
Convert Sorted Array to Binary Search Tree
᣾䔟
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
ܵᲿ
λܵ∄ȡ
Вⴰ
// LeetCode, Convert Sorted Array to Binary Search Tree
// ܵ⇪∄喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
TreeNode* sortedArrayToBST (vector<int>& num) {
return sortedArrayToBST(num.begin(), num.end());
}
template<typename RandomAccessIterator>
TreeNode* sortedArrayToBST (RandomAccessIterator first,
RandomAccessIterator last) {
const auto length = distance(first, last);
if (length <= 0) return nullptr;
// ㏷ₑᲐХ
// ̸᫨षᎥ
auto mid = first + length / 2;
TreeNode* root = new TreeNode (*mid);
root->left = sortedArrayToBST(first, mid);
root->right = sortedArrayToBST(mid + 1, last);
return root;
}
};

---

5.3
λࣸᴔឭᵀ
113
Ⱗڢ题Ⱍ
• Convert Sorted List to Binary Search Tree喌㻰§5.3.5
5.3.5
Convert Sorted List to Binary Search Tree
᣾䔟
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced
BST.
ܵᲿ
䔈题̹̯̽题ㆪѫ喌ѵ᭞ࢄ䨭㶗̼㘬䮾ᱩ䃮䬝喌㔻㜙䶥ी̺⮳λܵ∄ᓴ䶪䰯㺰RandomAccessIt-
erator喌ఏₓݼ䲑⮳᫨∄̼䔱⩗ᱛ题ȡ
ႇ౗̯⻼㜙Ꮔी̹ (bottom-up) ⮳᫨∄喌㻰http://leetcode.com/2010/11/convert-sorted-list-to-balanced-
binary.html
ܵ⇪∄喌㜙䶥ी̺
ܵ⇪∄喌ㆪѫν Convert Sorted Array to Binary Search Tree喌㜙䶥ी̺喌฼ᱱᏕO(n log n)ȡ
// LeetCode, Convert Sorted List to Binary Search Tree
// ܵ⇪∄喌ㆪѫν Convert Sorted Array to Binary Search Tree喌
// 㜙䶥ी̺喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
TreeNode* sortedListToBST (ListNode* head) {
return sortedListToBST (head, listLength (head));
}
TreeNode* sortedListToBST (ListNode* head, int len) {
if (len == 0) return nullptr;
if (len == 1) return new TreeNode (head->val);
TreeNode* root = new TreeNode (nth_node (head, len / 2 + 1)->val);
root->left = sortedListToBST (head, len / 2);
root->right = sortedListToBST (nth_node (head, len / 2 + 2),
(len - 1) / 2);
return root;
}
int listLength (ListNode* node) {
int n = 0;
while(node) {
++n;
node = node->next;

---

114
せ5 』
ᵀ
}
return n;
}
ListNode* nth_node (ListNode* node, int n) {
while (--n)
node = node->next;
return node;
}
};
㜙Ꮔी̹
// LeetCode, Convert Sorted List to Binary Search Tree
// bottom-up喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
TreeNode *sortedListToBST(ListNode *head) {
int len = 0;
ListNode *p = head;
while (p) {
len++;
p = p->next;
}
return sortedListToBST(head, 0, len - 1);
}
private:
TreeNode* sortedListToBST(ListNode*& list, int start, int end) {
if (start > end) return nullptr;
int mid = start + (end - start) / 2;
TreeNode *leftChild = sortedListToBST(list, start, mid - 1);
TreeNode *parent = new TreeNode(list->val);
parent->left = leftChild;
list = list->next;
parent->right = sortedListToBST(list, mid + 1, end);
return parent;
}
};
Ⱗڢ题Ⱍ
• Convert Sorted Array to Binary Search Tree喌㻰§5.3.4
5.4
λࣸᵀ⮳䕁ᒁ
λࣸᵀ᭞̯͙䕁ᒁ⮳᪟ᢝ㐂Ჳ喌ఏₓ᭞̯͙⩗Ე㔲ᄎ䕁ᒁᕌ㐣㘬ߊ⮳㐌Ң᪟ᢝ㐂Ჳȡ

---

5.4
λࣸᵀ⮳䕁ᒁ
115
䕁ᒁ̯჉᭞⌠᥋喈㻰§10.12.5㞱Ć⌠᥋̽䕁ᒁ⮳ࡩݚć喉喌⩠ν౗λࣸᵀ̹喌䕁ᒁ⮳ঢ䖂ᰣ⊂ϊ喌
ఏₓᱛ㞱⩗Ćλࣸᵀ⮳䕁ᒁćҋͩᴶ题喌㔻̼᭞Ćλࣸᵀ⮳⌠᥋ć喌ᅬバᱛ㞱ᝯ᰸⮳テ∄䘬ᆍν⌠᥋ȡ
λࣸᵀ⮳ٷᎾȠ͜ᎾȠऽᎾ䕼ࢵ䘬ञДⰺ։᭞DFS喌ₓๅ䔇᰸ڥЅ䶩Ꮎ⮳⌠Ꮥчٷ䕼ࢵ喌ڠ᰸
3! = 6 ⻼ȡڥЅ 3 ⻼䶩Ꮎ᭞root->r->l喌r->root->l, r->l->rootȡ
5.4.1
Minimum Depth of Binary Tree
᣾䔟
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest
leaf node.
ܵᲿ
ᬏ
䕁ᒁ❷
// LeetCode, Minimum Depth of Binary Tree
// 䕁ᒁ❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
int minDepth(const TreeNode *root) {
return minDepth(root, false);
}
private:
static int minDepth(const TreeNode *root, bool hasbrother) {
if (!root) return hasbrother ? INT_MAX : 0;
return 1 + min(minDepth(root->left, root->right != NULL),
minDepth(root->right, root->left != NULL));
}
};
䔜В❷
// LeetCode, Minimum Depth of Binary Tree
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
int minDepth(TreeNode* root) {
if (root == nullptr)
return 0;
int result = INT_MAX;
stack<pair<TreeNode*, int>> s;

---

116
せ5 』
ᵀ
s.push(make_pair(root, 1));
while (!s.empty()) {
auto node = s.top().first;
auto depth = s.top().second;
s.pop();
if (node->left == nullptr && node->right == nullptr)
result = min(result, depth);
if (node->left && result > depth) // ⌠Ꮥᣖݥ喌ޙ᳌
s.push(make_pair(node->left, depth + 1));
if (node->right && result > depth) // ⌠Ꮥᣖݥ喌ޙ᳌
s.push(make_pair(node->right, depth + 1));
}
return result;
}
};
Ⱗڢ题Ⱍ
• Maximum Depth of Binary Tree喌㻰§5.4.2
5.4.2
Maximum Depth of Binary Tree
᣾䔟
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Maximum Depth of Binary Tree
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
int maxDepth(TreeNode *root) {
if (root == nullptr) return 0;
return max(maxDepth(root->left), maxDepth(root->right)) + 1;
}
};

---

5.4
λࣸᵀ⮳䕁ᒁ
117
Ⱗڢ题Ⱍ
• Minimum Depth of Binary Tree喌㻰§5.4.1
5.4.3
Path Sum
᣾䔟
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
values along the path equals the given sum.
For example: Given the below binary tree and sum = 22,
5
/ \
4
8
/
/ \
11
13
4
/
\
\
7
2
1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
ܵᲿ
题Ⱍङ㺰ⅱ䔃఍true ᝅ㔴false喌ఏₓ̼䰯㺰䃟ᒄ䌞ᒳȡ
⩠νङ䰯㺰ⅱܩ̯͙㐂᳋喌ఏₓ喌ᒂጕȠढЪᘾ̯Ḥၿᵀⅱݟε␐ᘾ㐂᳋喌䘬ञДࣹᬥreturnȡ
⩠ν题Ⱍ⇐᰸䄣㞱◨⮳᪟ᢝ̯჉᭞ₒ᪣᪟喌ᓴ䶪㺰䊟ݟथၿ㞱◨᝼㘬ݓ᫜喌ఏₓ͜䕃⇐∄ޙ᳌喌
ङ㘬䔊㵻ᱣ㉏⌠᥋ȡ
Вⴰ
// LeetCode, Path Sum
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
bool hasPathSum(TreeNode *root, int sum) {
if (root == nullptr) return false;
if (root->left == nullptr && root->right == nullptr) // leaf
return sum == root->val;
return hasPathSum(root->left, sum - root->val)
|| hasPathSum(root->right, sum - root->val);
}
};
Ⱗڢ题Ⱍ
• Path Sum II喌㻰§5.4.4

---

118
せ5 』
ᵀ
5.4.4
Path Sum II
᣾䔟
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
For example: Given the below binary tree and sum = 22,
5
/ \
4
8
/
/ \
11
13
4
/
\
/ \
7
2
5
1
return
[
[5,4,11,2],
[5,8,4,5]
]
ܵᲿ
䌎̹̯题Ⱗ℃喌ᱛ题᭞ⅱ䌞ᒳᱛ䏚ȡ̓㺰ⅱܩᝯ᰸㐂᳋喌ጕၿᵀⅱݟε␐ᘾ㐂᳋喌̼㘬return喌
㺰ᣔⱯⅱढၿᵀȡ
Вⴰ
// LeetCode, Path Sum II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
vector<vector<int> > pathSum(TreeNode *root, int sum) {
vector<vector<int> > result;
vector<int> cur; // ͜䬣㐂᳋
pathSum(root, sum, cur, result);
return result;
}
private:
void pathSum(TreeNode *root, int gap, vector<int> &cur,
vector<vector<int> > &result) {
if (root == nullptr) return;
cur.push_back(root->val);
if (root->left == nullptr && root->right == nullptr) { // leaf
if (gap == root->val)
result.push_back(cur);
}
pathSum(root->left, gap - root->val, cur, result);
pathSum(root->right, gap - root->val, cur, result);

---

5.4
λࣸᵀ⮳䕁ᒁ
119
cur.pop_back();
}
};
Ⱗڢ题Ⱍ
• Path Sum喌㻰§5.4.3
5.4.5
Binary Tree Maximum Path Sum
᣾䔟
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree. For example: Given the below binary tree,
1
/ \
2
3
Return 6.
ܵᲿ
䔈题ᒷ䯭喌䌞ᒳञДϽЪᘾ㞱◨ᐯ໺喌ݟЪᘾ㞱◨㐂᲎ȡ
ञДݘ⩗Ćᰯ๖䔍㐜ၿᎾ݆঻ć䬝题⮳ᕌ䌞喌㻰せ§13.2㞱ȡັ᳋䄣Array ङ᰸̯͙᫨ी⮳䄌喌䗒
ͷ Binary Tree ڥჍङ᭞ጕȠढ͓͙᫨ी㔻ጡ喌ᝀЛ䰯㺰℃䒲͓͙᫨ी̹⮳իȡ
̼䓶喌Array ञДϽ๣ݟᅭ䕼ࢵ喌䗒ͷ Binary Tree ᔽͷߍ঑喌ᝀЛञД䛶⩗Binary Tree ᰯ፧⩗
⮳dfs Ე䔊㵻䕼ࢵȡٷテܩጕढၿᵀ⮳㐂᳋L ঻R喌ັ᳋L ๖ν 0喌䗒ͷᄨऽ㐜㐂᳋᭞᰸ݘ⮳喌ᝀЛ
ߏ̹ L喌ັ᳋R ๖ν 0喌ᄨऽ㐜㐂᳋Ύ᭞᰸ݘ⮳喌㐖㐜ߏ̹ Rȡ
Вⴰ
// LeetCode, Binary Tree Maximum Path Sum
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
int maxPathSum(TreeNode *root) {
max_sum = INT_MIN;
dfs(root);
return max_sum;
}
private:
int max_sum;
int dfs(const TreeNode *root) {
if (root == nullptr) return 0;
int l = dfs(root->left);
int r = dfs(root->right);

---

120
せ5 』
ᵀ
int sum = root->val;
if (l > 0) sum += l;
if (r > 0) sum += r;
max_sum = max(max_sum, sum);
return max(r, l) > 0 ? max(r, l) + root->val : root->val;
}
};
∗ᘾ喌ᰯऽreturn ⮳ᬥՈ喌ङ䔃఍̯͙᫨ी̹⮳ի喌ͩϯͷ喟䔈᭞ఏͩ౗䕁ᒁ͜喌ङ㘬ी❥㞱◨
䔃఍喌̼ञ㘬ႇ౗L->root->R ⮳䌞ᒳ喌ङञ㘬᭞L->root ᝅR->rootȡ
Ⱗڢ题Ⱍ
• Maximum Subarray喌㻰§13.2
5.4.6
Populating Next Right Pointers in Each Node
᣾䔟
Given a binary tree
struct TreeLinkNode {
int val;
TreeLinkNode *left, *right, *next;
TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
should be set to NULL.
Initially, all next pointers are set to NULL.
Note:
• You may only use constant extra space.
• You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent
has two children).
For example, Given the following perfect binary tree,
1
/
\
2
3
/ \
/ \
4
5
6
7
After calling your function, the tree should look like:
1 -> NULL
/
\
2 -> 3 -> NULL
/ \
/ \
4->5->6->7 -> NULL

---

5.4
λࣸᵀ⮳䕁ᒁ
121
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Populating Next Right Pointers in Each Node
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
void connect(TreeLinkNode *root) {
connect(root, NULL);
}
private:
void connect(TreeLinkNode *root, TreeLinkNode *sibling) {
if (root == nullptr)
return;
else
root->next = sibling;
connect(root->left, root->right);
if (sibling)
connect(root->right, sibling->left);
else
connect(root->right, nullptr);
}
};
Ⱗڢ题Ⱍ
• Populating Next Right Pointers in Each Node II喌㻰§5.1.12
5.4.7
Sum Root to Leaf Numbers
᣾䔟
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
1
/ \
2
3
The root-to-leaf path 1->2 represents the number 12. The root-to-leaf path 1->3 represents the number
13.
Return the sum = 12 + 13 = 25.

---

122
せ5 』
ᵀ
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Decode Ways
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(logn)
class Solution {
public:
int sumNumbers(TreeNode *root) {
return dfs(root, 0);
}
private:
int dfs(TreeNode *root, int sum) {
if (root == nullptr) return 0;
if (root->left == nullptr && root->right == nullptr)
return sum * 10 + root->val;
return dfs(root->left, sum * 10 + root->val) +
dfs(root->right, sum * 10 + root->val);
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

せ6 』
ᣁᎾ
6.1
Merge Sorted Array
᣾䔟
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note: You may assume that A has enough space to hold additional elements from B. The number of
elements initialized in A and B are m and n respectively.
ܵᲿ
ᬏ
Вⴰ
//LeetCode, Merge Sorted Array
// ᬥ䬣฼ᱱᏕO(m+n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void merge(vector<int>& A, int m, vector<int>& B, int n) {
int ia = m - 1, ib = n - 1, icur = m + n - 1;
while(ia >= 0 && ib >= 0) {
A[icur--] = A[ia] >= B[ib] ? A[ia--] : B[ib--];
}
while(ib >= 0) {
A[icur--] = B[ib--];
}
}
};
Ⱗڢ题Ⱍ
• Merge Two Sorted Lists喌㻰§6.2
• Merge k Sorted Lists喌㻰§6.3
123

---

124
せ6 』
ᣁᎾ
6.2
Merge Two Sorted Lists
᣾䔟
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.
ܵᲿ
ᬏ
Вⴰ
//LeetCode, Merge Two Sorted Lists
// ᬥ䬣฼ᱱᏕO(min(m,n))喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
if (l1 == nullptr) return l2;
if (l2 == nullptr) return l1;
ListNode dummy(-1);
ListNode *p = &dummy;
for (; l1 != nullptr && l2 != nullptr; p = p->next) {
if (l1->val > l2->val) { p->next = l2; l2 = l2->next; }
else { p->next = l1; l1 = l1->next; }
}
p->next = l1 != nullptr ? l1 : l2;
return dummy.next;
}
};
Ⱗڢ题Ⱍ
• Merge Sorted Array §6.1
• Merge k Sorted Lists喌㻰§6.3
6.3
Merge k Sorted Lists
᣾䔟
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
ܵᲿ
ञД฼⩗Merge Two Sorted Lists喈㻰§6.2喉⮳ܬ᪟

---

6.4
Insertion Sort List
125
Вⴰ
//LeetCode, Merge k Sorted Lists
// ᬥ䬣฼ᱱᏕO(n1+n2+...)喌⾩䬣฼ᱱᏕO(1)
// TODO: щ䊴ᬥ
class Solution {
public:
ListNode *mergeKLists(vector<ListNode *> &lists) {
if (lists.size() == 0) return nullptr;
ListNode *p = lists[0];
for (int i = 1; i < lists.size(); i++) {
p = mergeTwoLists(p, lists[i]);
}
return p;
}
// Merge Two Sorted Lists
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
ListNode head(-1);
for (ListNode* p = &head; l1 != nullptr || l2 != nullptr; p = p->next) {
int val1 = l1 == nullptr ? INT_MAX : l1->val;
int val2 = l2 == nullptr ? INT_MAX : l2->val;
if (val1 <= val2) {
p->next = l1;
l1 = l1->next;
} else {
p->next = l2;
l2 = l2->next;
}
}
return head.next;
}
};
Ⱗڢ题Ⱍ
• Merge Sorted Array §6.1
• Merge Two Sorted Lists喌㻰§6.2
6.4
Insertion Sort List
᣾䔟
Sort a linked list using insertion sort.
ܵᲿ
ᬏ

---

126
せ6 』
ᣁᎾ
Вⴰ
// LeetCode, Insertion Sort List
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
ListNode *insertionSortList(ListNode *head) {
ListNode dummy(INT_MIN);
//dummy.next = head;
for (ListNode *cur = head; cur != nullptr;) {
auto pos = findInsertPos(&dummy, cur->val);
ListNode *tmp = cur->next;
cur->next = pos->next;
pos->next = cur;
cur = tmp;
}
return dummy.next;
}
ListNode* findInsertPos(ListNode *head, int x) {
ListNode *pre = nullptr;
for (ListNode *cur = head; cur != nullptr && cur->val <= x;
pre = cur, cur = cur->next)
;
return pre;
}
};
Ⱗڢ题Ⱍ
• Sort List, 㻰§6.5
6.5
Sort List
᣾䔟
Sort a linked list in O(nlogn) time using constant space complexity.
ܵᲿ
፧᪟⾩䬣̓ O(nlogn)喌ࢄ䨭㶗䔱ष⩗ᒁᎥᣁᎾ喌ࣻी䨭㶗䔱ष⩗ᔚ䕎ᣁᎾȡᱛ题ञД฼⩗”Merge
Two Sorted Lists” ⮳Вⴰȡ
Вⴰ
// LeetCode, Sort List
// ᒁᎥᣁᎾ喌ᬥ䬣฼ᱱᏕO(nlogn)喌⾩䬣฼ᱱᏕO(1)
class Solution {

---

6.6
First Missing Positive
127
public:
ListNode *sortList(ListNode *head) {
if (head == NULL || head->next == NULL)return head;
// ᔚᚑᠶ䦷ឭݟ͜䬣㞱◨
ListNode *fast = head, *slow = head;
while (fast->next != NULL && fast->next->next != NULL) {
fast = fast->next->next;
slow = slow->next;
}
// ᫜ᐯ
fast = slow;
slow = slow->next;
fast->next = NULL;
ListNode *l1 = sortList(head);
// ݼࡹ⃤ᣁᎾ
ListNode *l2 = sortList(slow);
// ऽࡹ⃤ᣁᎾ
return mergeTwoLists(l1, l2);
}
// Merge Two Sorted Lists
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
ListNode dummy(-1);
for (ListNode* p = &dummy; l1 != nullptr || l2 != nullptr; p = p->next) {
int val1 = l1 == nullptr ? INT_MAX : l1->val;
int val2 = l2 == nullptr ? INT_MAX : l2->val;
if (val1 <= val2) {
p->next = l1;
l1 = l1->next;
} else {
p->next = l2;
l2 = l2->next;
}
}
return dummy.next;
}
};
Ⱗڢ题Ⱍ
• Insertion Sort List喌㻰§6.4
6.6
First Missing Positive
᣾䔟
Given an unsorted integer array, find the first missing positive integer.
For example, Given [1,2,0] return 3, and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.

---

128
せ6 』
ᣁᎾ
ܵᲿ
ᱛ䉗̹᭞ᶥᣁᎾ(bucket sort)喌⃾ᒂA[i]!= i+1 ⮳ᬥՈ喌ᄵA[i] ̽ A[A[i]-1] ϓᢑ喌Ⱓݟᬏ∄ϓ
ᢑͩₑ喌㏷ₑᲐХ᭞A[i]== A[A[i]-1]ȡ
Вⴰ
// LeetCode, First Missing Positive
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int firstMissingPositive(vector<int>& nums) {
bucket_sort(nums);
for (int i = 0; i < nums.size(); ++i)
if (nums[i] != (i + 1))
return i + 1;
return nums.size() + 1;
}
private:
static void bucket_sort(vector<int>& A) {
const int n = A.size();
for (int i = 0; i < n; i++) {
while (A[i] != i + 1) {
if (A[i] <= 0 || A[i] > n || A[i] == A[A[i] - 1])
break;
swap(A[i], A[A[i] - 1]);
}
}
}
};
Ⱗڢ题Ⱍ
• Sort Colors, 㻰§6.7
6.7
Sort Colors
᣾䔟
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are
adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library’s sort function for this problem.
Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.

---

6.7
Sort Colors
129
First, iterate the array counting number of 0’s, 1’s, and 2’s, then overwrite array with total number of 0’s,
then 1’s and followed by 2’s.
Could you come up with an one-pass algorithm using only constant space?
ܵᲿ
⩠ν 0, 1, 2 䲍፧㉖܀喌仅ٷᘢݟ䃐᪟ᣁᎾ(counting sort)喌ѵ䰯㺰រ᣾͓䕼喌̼さष题Ⱍ㺰ⅱȡ
⩠νङ᰸̸⻼䷋㞡喌ञД䃭㒝͓͙ index喌̯͙᭞red ⮳index喌̯͙᭞blue ⮳index喌͓䓨ᒯ͜
䬣䊟ȡᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)ȡ
せ3 ⻼ᕌ䌞喌ݘ⩗ᔚ䕎ᣁᎾ䛻partition ⮳ᕌᘢ喌せ̯⁐ᄵ᪟㏳ᠸ0 ܵޡ喌せλ⁐ᠸ1 ܵޡ喌ᣁᎾ
Ⴛ℄喌ञДᣗᎮݟn ⻼䷋㞡喌⃾⻼䷋㞡᰸䛼฼ٲ㉏⮳ᗴۤȡ
Вⴰ1
// LeetCode, Sort Colors
// Counting Sort
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void sortColors(vector<int>& A) {
int counts[3] = { 0 }; // 䃟ᒄ⃾͙䷋㞡ܩ⣟⮳⁐᪟
for (int i = 0; i < A.size(); i++)
counts[A[i]]++;
for (int i = 0, index = 0; i < 3; i++)
for (int j = 0; j < counts[i]; j++)
A[index++] = i;
}
};
Вⴰ2
// LeetCode, Sort Colors
// ࣻᠶ䦷喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void sortColors(vector<int>& A) {
// ̯͙᭞red ⮳index喌̯͙᭞blue ⮳index喌͓䓨ᒯ͜䬣䊟
int red = 0, blue = A.size() - 1;
for (int i = 0; i < blue + 1;) {
if (A[i] == 0)
swap(A[i++], A[red++]);
else if (A[i] == 2)
swap(A[i], A[blue--]);
else

---

130
せ6 』
ᣁᎾ
i++;
}
}
};
Вⴰ3
// LeetCode, Sort Colors
// use partition()
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void sortColors(vector<int>& nums) {
partition(partition(nums.begin(), nums.end(), bind1st(equal_to<int>(), 0)),
nums.end(), bind1st(equal_to<int>(), 1));
}
};
Вⴰ4
// LeetCode, Sort Colors
// 䛼᫟Ⴭ⣟partition()
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
void sortColors(vector<int>& nums) {
partition(partition(nums.begin(), nums.end(), bind1st(equal_to<int>(), 0)),
nums.end(), bind1st(equal_to<int>(), 1));
}
private:
template<typename ForwardIterator, typename UnaryPredicate>
ForwardIterator partition(ForwardIterator first, ForwardIterator last,
UnaryPredicate pred) {
auto pos = first;
for (; first != last; ++first)
if (pred(*first))
swap(*first, *pos++);
return pos;
}
};
Ⱗڢ题Ⱍ
• First Missing Positive, 㻰§6.6

---

せ7 』
ᴔឭ
7.1
Search for a Range
᣾䔟
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
ܵᲿ
ጡ㏾ᣁຬεᎾ喌⩗λܵᴔឭȡ
Ү⩗STL
// LeetCode, Search for a Range
// ֦ᜁ⮳։∄喌Ү⩗STL
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> searchRange(vector<int>& nums, int target) {
const int l = distance(nums.begin(), lower_bound(nums.begin(), nums.end(), target));
const int u = distance(nums.begin(), prev(upper_bound(nums.begin(), nums.end(), target
if (nums[l] != target) // not found
return vector<int> { -1, -1 };
else
return vector<int> { l, u };
}
};
䛼᫟Ⴭ⣟lower_bound ঻upper_bound
// LeetCode, Search for a Range
// 䛼᫟Ⴭ⣟lower_bound ঻upper_bound
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
131

---

132
せ7 』
ᴔឭ
public:
vector<int> searchRange (vector<int>& nums, int target) {
auto lower = lower_bound(nums.begin(), nums.end(), target);
auto uppper = upper_bound(lower, nums.end(), target);
if (lower == nums.end() || *lower != target)
return vector<int> { -1, -1 };
else
return vector<int> {distance(nums.begin(), lower), distance(nums.begin(), prev(upp
}
template<typename ForwardIterator, typename T>
ForwardIterator lower_bound (ForwardIterator first,
ForwardIterator last, T value) {
while (first != last) {
auto mid = next(first, distance(first, last) / 2);
if (value > *mid)
first = ++mid;
else
last = mid;
}
return first;
}
template<typename ForwardIterator, typename T>
ForwardIterator upper_bound (ForwardIterator first,
ForwardIterator last, T value) {
while (first != last) {
auto mid = next(first, distance (first, last) / 2);
if (value >= *mid)
first = ++mid;
// ̽ lower_bound ϴₓ̼ऻ
else
last = mid;
}
return first;
}
};
Ⱗڢ题Ⱍ
• Search Insert Position, 㻰§7.2
7.2
Search Insert Position
᣾䔟
Given a sorted array and a target value, return the index if the target is found. If not, return the index
where it would be if it were inserted in order.
You may assume no duplicates in the array.

---

7.3
Search a 2D Matrix
133
Here are few examples.
[1,3,5,6], 5 →2
[1,3,5,6], 2 →1
[1,3,5,6], 7 →4
[1,3,5,6], 0 →0
ܵᲿ
ࢢstd::lower_bound()ȡ
Вⴰ
// LeetCode, Search Insert Position
// 䛼᫟Ⴭ⣟lower_bound
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int searchInsert(vector<int>& nums, int target) {
return distance(nums.begin(), lower_bound(nums.begin(), nums.end(), target));
}
template<typename ForwardIterator, typename T>
ForwardIterator lower_bound (ForwardIterator first,
ForwardIterator last, T value) {
while (first != last) {
auto mid = next(first, distance(first, last) / 2);
if (value > *mid)
first = ++mid;
else
last = mid;
}
return first;
}
};
Ⱗڢ题Ⱍ
• Search for a Range, 㻰§7.1
7.3
Search a 2D Matrix
᣾䔟
Write an efficient algorithm that searches for a value in an m × n matrix. This matrix has the following
properties:
• Integers in each row are sorted from left to right.
• The first integer of each row is greater than the last integer of the previous row.

---

134
せ7 』
ᴔឭ
For example, Consider the following matrix:
[
[1,
3,
5,
7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
Given target = 3, return true.
ܵᲿ
λܵᴔឭȡ
Вⴰ
// LeetCode, Search a 2D Matrix
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool searchMatrix(const vector<vector<int>>& matrix, int target) {
if (matrix.empty()) return false;
const size_t
m = matrix.size();
const size_t n = matrix.front().size();
int first = 0;
int last = m * n;
while (first < last) {
int mid = first + (last - first) / 2;
int value = matrix[mid / n][mid % n];
if (value == target)
return true;
else if (value < target)
first = mid + 1;
else
last = mid;
}
return false;
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

せ8 』
ᯣߊ᳉ͭ∄
8.1
Subsets
᣾䔟
Given a set of distinct integers, S, return all possible subsets.
Note:
• Elements in a subset must be in non-descending order.
• The solution set must not contain duplicate subsets.
For example, If S = [1,2,3], a solution is:
[
[3],
[1],
[2],
[1,2,3],
[1,3],
[2,3],
[1,2],
[]
]
8.1.1
䕁ᒁ
෍䛾Ჳ䕏∄
⃾͙ٲ㉏喌䘬᰸͓⻼䔸᠘喌䔸ᝅ㔴̼䔸ȡ
// LeetCode, Subsets
// ෍䛾Ჳ䕏∄喌⌠᥋喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > subsets(vector<int> &S) {
sort(S.begin(), S.end());
// 䓂ܩ㺰ⅱ᰸Ꮎ
vector<vector<int> > result;
vector<int> path;
subsets(S, path, 0, result);
return result;
135

---

136
せ8 』
ᯣߊ᳉ͭ∄
}
private:
static void subsets(const vector<int> &S, vector<int> &path, int step,
vector<vector<int> > &result) {
if (step == S.size()) {
result.push_back(path);
return;
}
// ̼䔸S[step]
subsets(S, path, step + 1, result);
// 䔸S[step]
path.push_back(S[step]);
subsets(S, path, step + 1, result);
path.pop_back();
}
};
Ѽी䛾∄
ᐯ̯͙Ѽी䛾bool selected[n]喌⃾͙ٲ㉏ञД䔸ᝅ㔴̼䔸ȡ
// LeetCode, Subsets
// Ѽी䛾∄喌⌠᥋喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > subsets(vector<int> &S) {
sort(S.begin(), S.end());
// 䓂ܩ㺰ⅱ᰸Ꮎ
vector<vector<int> > result;
vector<bool> selected(S.size(), false);
subsets(S, selected, 0, result);
return result;
}
private:
static void subsets(const vector<int> &S, vector<bool> &selected, int step,
vector<vector<int> > &result) {
if (step == S.size()) {
vector<int> subset;
for (int i = 0; i < S.size(); i++) {
if (selected[i]) subset.push_back(S[i]);
}
result.push_back(subset);
return;
}
// ̼䔸S[step]
selected[step] = false;
subsets(S, selected, step + 1, result);
// 䔸S[step]
selected[step] = true;
subsets(S, selected, step + 1, result);

---

8.1
Subsets
137
}
};
8.1.2
䔜В
෍䛾Ჳ䕏∄
// LeetCode, Subsets
// 䔜В❷喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > subsets(vector<int> &S) {
sort(S.begin(), S.end()); // 䓂ܩ㺰ⅱ᰸Ꮎ
vector<vector<int> > result(1);
for (auto elem : S) {
result.reserve(result.size() * 2);
auto half = result.begin() + result.size();
copy(result.begin(), half, back_inserter(result));
for_each(half, result.end(), [&elem](decltype(result[0]) &e){
e.push_back(elem);
});
}
return result;
}
};
λ䔊ݥ∄
ᱛ᫨∄⮳ݼ᣿᭞喚䯵ष⮳ٲ㉏̼䊴䓶int Ѽ᪟ȡ⩗̯͙ int ᪣᪟㶗⹩Ѽी䛾喌せi Ѽͩ 1喌݈㶗⹩
䔸᠘S[i]喌ͩ 0 ݈̼䔸᠘ȡҺັS={A,B,C,D}喌݈0110=6 㶗⹩ၿ䯵{B,C}ȡ
䔈⻼᫨∄ᰯ጖່ȡఏͩႲ̼ϴ㘬⩎᜿ၿ䯵喌䔇㘬᫨Ӯ⮳㶗⹩䯵ष⮳ᎥȠϓȠጝへ䯵ष䓿テȡ䃭͓
͙䯵ष⮳Ѽी䛾ܵݚͩ B1 ঻B2喌݈B1 ∪B2, B1 ∩B2, B1△B2 ܵݚᄨᏃ䯵ष⮳ᎥȠϓȠᄨ⼟ጝȡ
λ䔊ݥ∄喌ΎञДⰺ։᭞Ѽी䛾∄喌ङ̼䓶ᰣߏчࡅȡ
// LeetCode, Subsets
// λ䔊ݥ∄喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > subsets(vector<int> &S) {
sort(S.begin(), S.end()); // 䓂ܩ㺰ⅱ᰸Ꮎ
vector<vector<int> > result;
const size_t n = S.size();
vector<int> v;
for (size_t i = 0; i < 1 << n; i++) {
for (size_t j = 0; j < n; j++) {
if (i & 1 << j) v.push_back(S[j]);
}
result.push_back(v);
v.clear();

---

138
せ8 』
ᯣߊ᳉ͭ∄
}
return result;
}
};
Ⱗڢ题Ⱍ
• Subsets II喌㻰§8.2
8.2
Subsets II
᣾䔟
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order. The solution set must not contain duplicate
subsets. For example, If S = [1,2,2], a solution is:
[
[2],
[1],
[1,2,2],
[2,2],
[1,2],
[]
]
ܵᲿ
䔈题᰸䛼฼ٲ㉏喌ѵᱛ䉗̹喌䌎̹̯题ᒷㆪѫ喌̹̯题͜ٲ㉏⇐᰸䛼฼喌Ⱗᒂν⃾͙ٲ㉏ङ㘬䔸
0 ᝅ1 ⁐喌䔈䛻មٴݟε⃾͙ٲ㉏ञД䔸0 ݟ㠔Ꭱ⁐㔻ጡȡ
8.2.1
䕁ᒁ
෍䛾Ჳ䕏∄
// LeetCode, Subsets II
// ෍䛾Ჳ䕏∄喌❷ᱛ1喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > subsetsWithDup(vector<int> &S) {
sort(S.begin(), S.end());
// ᓴ䶪ᣁᎾ
vector<vector<int> > result;
vector<int> path;
dfs(S, S.begin(), path, result);

---

8.2
Subsets II
139
return result;
}
private:
static void dfs(const vector<int> &S, vector<int>::iterator start,
vector<int> &path, vector<vector<int> > &result) {
result.push_back(path);
for (auto i = start; i < S.end(); i++) {
if (i != start && *i == *(i-1)) continue;
path.push_back(*i);
dfs(S, i + 1, path, result);
path.pop_back();
}
}
};
// LeetCode, Subsets II
// ෍䛾Ჳ䕏∄喌❷ᱛ2喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > subsetsWithDup(vector<int> &S) {
vector<vector<int> > result;
sort(S.begin(), S.end()); // ᓴ䶪ᣁᎾ
unordered_map<int, int> count_map; // 䃟ᒄ⃾͙ٲ㉏⮳ܩ⣟⁐᪟
for_each(S.begin(), S.end(), [&count_map](int e) {
if (count_map.find(e) != count_map.end())
count_map[e]++;
else
count_map[e] = 1;
});
// ᄵmap 䛻⮳pair ᠦ䉌ݟ̯͙ vector 䛻
vector<pair<int, int> > elems;
for_each(count_map.begin(), count_map.end(),
[&elems](const pair<int, int> &e) {
elems.push_back(e);
});
sort(elems.begin(), elems.end());
vector<int> path; // ͜䬣㐂᳋
subsets(elems, 0, path, result);
return result;
}
private:
static void subsets(const vector<pair<int, int> > &elems,
size_t step, vector<int> &path, vector<vector<int> > &result) {
if (step == elems.size()) {
result.push_back(path);
return;
}

---

140
せ8 』
ᯣߊ᳉ͭ∄
for (int i = 0; i <= elems[step].second; i++) {
for (int j = 0; j < i; ++j) {
path.push_back(elems[step].first);
}
subsets(elems, step + 1, path, result);
for (int j = 0; j < i; ++j) {
path.pop_back();
}
}
}
};
Ѽी䛾∄
// LeetCode, Subsets II
// Ѽी䛾∄喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > subsetsWithDup(vector<int> &S) {
vector<vector<int> > result; // ᓴ䶪ᣁᎾ
sort(S.begin(), S.end());
vector<int> count(S.back() - S.front() + 1, 0);
// 䃐テᝯ᰸ٲ㉏⮳͙᪟
for (auto i : S) {
count[i - S[0]]++;
}
// ⃾͙ٲ㉏䔸᠘ε้ᅀ͙
vector<int> selected(S.back() - S.front() + 1, -1);
subsets(S, count, selected, 0, result);
return result;
}
private:
static void subsets(const vector<int> &S, vector<int> &count,
vector<int> &selected, size_t step, vector<vector<int> > &result) {
if (step == count.size()) {
vector<int> subset;
for(size_t i = 0; i < selected.size(); i++) {
for (int j = 0; j < selected[i]; j++) {
subset.push_back(i+S[0]);
}
}
result.push_back(subset);
return;
}
for (int i = 0; i <= count[step]; i++) {
selected[step] = i;
subsets(S, count, selected, step + 1, result);
}
}

---

8.2
Subsets II
141
};
8.2.2
䔜В
෍䛾Ჳ䕏∄
// LeetCode, Subsets II
// ෍䛾Ჳ䕏∄
// ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > subsetsWithDup(vector<int> &S) {
sort(S.begin(), S.end()); // ᓴ䶪ᣁᎾ
vector<vector<int> > result(1);
size_t previous_size = 0;
for (size_t i = 0; i < S.size(); ++i) {
const size_t size = result.size();
for (size_t j = 0; j < size; ++j) {
if (i == 0 || S[i] != S[i-1] || j >= previous_size) {
result.push_back(result[j]);
result.back().push_back(S[i]);
}
}
previous_size = size;
}
return result;
}
};
λ䔊ݥ∄
// LeetCode, Subsets II
// λ䔊ݥ∄喌ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > subsetsWithDup(vector<int> &S) {
sort(S.begin(), S.end()); // ᓴ䶪ᣁᎾ
// ⩗set ࣪䛼喌̼㘬⩗unordered_set喌ఏͩ䓂ܩ㺰ⅱ᰸Ꮎ
set<vector<int> > result;
const size_t n = S.size();
vector<int> v;
for (size_t i = 0; i < 1U << n; ++i) {
for (size_t j = 0; j < n; ++j) {
if (i & 1 << j)
v.push_back(S[j]);
}
result.insert(v);
v.clear();
}
vector<vector<int> > real_result;

---

142
せ8 』
ᯣߊ᳉ͭ∄
copy(result.begin(), result.end(), back_inserter(real_result));
return real_result;
}
};
Ⱗڢ题Ⱍ
• Subsets喌㻰§8.1
8.3
Permutations
᣾䔟
Given a collection of numbers, return all possible permutations.
For example, [1,2,3] have the following permutations: [1,2,3], [1,3,2], [2,1,3], [2,3,1],
[3,1,2], and [3,2,1].
8.3.1
next_permutation()
֦ᜁ⮳։∄喌ञДⰣᣔҮ⩗std::next_permutation()ȡັ᳋᭞౗OJ 㒀〈̹喌ञД⩗䔈͙ API
֦͙ᜁ喛ັ᳋᭞౗䲑䄄͜喌䲑䄄Ⴧ㗞჉щ䃘ҏ䛼᫟Ⴭ⣟ȡ
Вⴰ
// LeetCode, Permutations
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > permute(vector<int> &num) {
vector<vector<int> > result;
sort(num.begin(), num.end());
do {
result.push_back(num);
} while(next_permutation(num.begin(), num.end()));
return result;
}
};
8.3.2
䛼᫟Ⴭ⣟next_permutation()
㻰せ§2.1.12 㞱ȡ

---

8.3
Permutations
143
Вⴰ
// LeetCode, Permutations
// 䛼᫟Ⴭ⣟next_permutation()
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<int> > permute(vector<int> &num) {
vector<vector<int> > result;
sort(num.begin(), num.end());
do {
result.push_back(num);
// 䄲⩗⮳᭞2.1.12 㞱⮳next_permutation()
// 㔻̼᭞std::next_permutation()
} while(next_permutation(num.begin(), num.end()));
return result;
}
};
8.3.3
䕁ᒁ
ᱛ题᭞ⅱ䌞ᒳᱛ䏚喌ⅱᝯ᰸解喌ܬ᪟ࣱ᪟䰯㺰ᴶ䃟ᒂݼ䊟ݟεਙₔ喌䔇䰯㺰͜䬣㐂᳋⮳ᑄ⩗喌ᰯ
㏷㐂᳋⮳ᑄ⩗ȡ
មᆄ㞱◨喌⃾⁐Ͻጕݟढ喌䔸̯͙⇐᰸ܩ⣟䓶⮳ٲ㉏ȡ
ᱛ题̼䰯㺰ݓ䛼喌ఏͩ⟥ᔰ㷴ᢑభ᭞̯䷆᰸ᅱ⁐⮳ᵀȡᩥ᪊ᲐХ᭞ᒂݼ䊟ݟεᰯऽ̯͙ٲ㉏ȡ
Вⴰ
// LeetCode, Permutations
// ⌠᥋喌෍䛾Ჳ䕏∄
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > permute(vector<int>& num) {
sort(num.begin(), num.end());
vector<vector<int>> result;
vector<int> path;
// ͜䬣㐂᳋
dfs(num, path, result);
return result;
}
private:
void dfs(const vector<int>& num, vector<int> &path,
vector<vector<int> > &result) {
if (path.size() == num.size()) {
// ᩥ᪊ᲐХ
result.push_back(path);
return;
}

---

144
せ8 』
ᯣߊ᳉ͭ∄
// មᆄ⟥ᔰ
for (auto i : num) {
// ᴔឭi ᭞ॕ౗path ͜ܩ⣟䓶
auto pos = find(path.begin(), path.end(), i);
if (pos == path.end()) {
path.push_back(i);
dfs(num, path, result);
path.pop_back();
}
}
}
};
Ⱗڢ题Ⱍ
• Next Permutation, 㻰§2.1.12
• Permutation Sequence, 㻰§2.1.13
• Permutations II, 㻰§8.4
• Combinations, 㻰§8.5
8.4
Permutations II
᣾䔟
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example, [1,1,2] have the following unique permutations: [1,1,2], [1,2,1], and [2,1,1].
8.4.1
next_permutation()
ⰣᣔҮ⩗std::next_permutation()喌Вⴰ̹̯̽题Ⱗऻȡ
8.4.2
䛼᫟Ⴭ⣟next_permutation()
䛼᫟Ⴭ⣟std::next_permutation()喌Вⴰ̹̯̽题Ⱗऻȡ
8.4.3
䕁ᒁ
䕁ᒁܬ᪟permute() ⮳ࣱ᪟p喌᭞͜䬣㐂᳋喌Ⴒ⮳䪮Ꮥࣷ㘬ᴶ䃟ᒂݼ䊟ݟεਙ̯ₔ喌⩗νݓ᫜
ᩥ᪊ᲐХȡ
មᆄ㞱◨喌⃾⁐Ͻᄾݟ๖喌䔸̯͙⇐᰸㷚⩗ٸ⮳ٲ㉏喌Ⱓݟᝯ᰸ٲ㉏㷚⩗ٸȡ
ᱛ题̼䰯㺰ݓ䛼喌ఏͩ⟥ᔰ㷴ᢑభ᭞̯䷆᰸ᅱ⁐⮳ᵀȡ

---

8.4
Permutations II
145
Вⴰ
// LeetCode, Permutations II
// ⌠᥋喌ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > permuteUnique(vector<int>& num) {
sort(num.begin(), num.end());
unordered_map<int, int> count_map; // 䃟ᒄ⃾͙ٲ㉏⮳ܩ⣟⁐᪟
for_each(num.begin(), num.end(), [&count_map](int e) {
if (count_map.find(e) != count_map.end())
count_map[e]++;
else
count_map[e] = 1;
});
// ᄵmap 䛻⮳pair ᠦ䉌ݟ̯͙ vector 䛻
vector<pair<int, int> > elems;
for_each(count_map.begin(), count_map.end(),
[&elems](const pair<int, int> &e) {
elems.push_back(e);
});
vector<vector<int>> result; // ᰯ㏷㐂᳋
vector<int> p;
// ͜䬣㐂᳋
n = num.size();
permute(elems.begin(), elems.end(), p, result);
return result;
}
private:
size_t n;
typedef vector<pair<int, int> >::const_iterator Iter;
void permute(Iter first, Iter last, vector<int> &p,
vector<vector<int> > &result) {
if (n == p.size()) {
// ᩥ᪊ᲐХ
result.push_back(p);
}
// មᆄ⟥ᔰ
for (auto i = first; i != last; i++) {
int count = 0; // 㐎䃐*i ౗p ͜ܩ⣟䓶้ᅀ⁐
for (auto j = p.begin(); j != p.end(); j++) {
if (i->first == *j) {
count ++;
}
}
if (count < i->second) {
p.push_back(i->first);
permute(first, last, p, result);

---

146
せ8 』
ᯣߊ᳉ͭ∄
p.pop_back(); // ᧓䨯ߗҋ喌䔃఍̹̯ᅱ
}
}
}
};
Ⱗڢ题Ⱍ
• Next Permutation, 㻰§2.1.12
• Permutation Sequence, 㻰§2.1.13
• Permutations, 㻰§8.3
• Combinations, 㻰§8.5
8.5
Combinations
᣾䔟
Given two integers n and k, return all possible combinations of k numbers out of 1...n.
For example, If n = 4 and k = 2, a solution is:
[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]
8.5.1
䕁ᒁ
// LeetCode, Combinations
// ⌠᥋喌䕁ᒁ
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > combine(int n, int k) {
vector<vector<int> > result;
vector<int> path;
dfs(n, k, 1, 0, path, result);
return result;
}
private:
// start喌ᐯ໺⮳᪟, cur喌ጡ㏾䔸᠘⮳᪟Ⱍ
static void dfs(int n, int k, int start, int cur,
vector<int> &path, vector<vector<int> > &result) {
if (cur == k) {
result.push_back(path);

---

8.6
Letter Combinations of a Phone Number
147
}
for (int i = start; i <= n; ++i) {
path.push_back(i);
dfs(n, k, i + 1, cur + 1, path, result);
path.pop_back();
}
}
};
8.5.2
䔜В
// LeetCode, Combinations
// use prev_permutation()
// ᬥ䬣฼ᱱᏕO((n-k)!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > combine(int n, int k) {
vector<int> values(n);
iota(values.begin(), values.end(), 1);
vector<bool> select(n, false);
fill_n(select.begin(), k, true);
vector<vector<int> > result;
do{
vector<int> one(k);
for (int i = 0, index = 0; i < n; ++i)
if (select[i])
one[index++] = values[i];
result.push_back(one);
} while(prev_permutation(select.begin(), select.end()));
return result;
}
};
Ⱗڢ题Ⱍ
• Next Permutation, 㻰§2.1.12
• Permutation Sequence, 㻰§2.1.13
• Permutations, 㻰§8.3
• Permutations II, 㻰§8.4
8.6
Letter Combinations of a Phone Number
᣾䔟
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

---

148
せ8 』
ᯣߊ᳉ͭ∄
భ8-1
Phone Keyboard
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note: Although the above answer is in lexicographical order, your answer could be in any order you
want.
ܵᲿ
ᬏ
8.6.1
䕁ᒁ
// LeetCode, Letter Combinations of a Phone Number
// ᬥ䬣฼ᱱᏕO(3^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
const vector<string> keyboard { " ", "", "abc", "def", // '0','1','2',...
"ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
vector<string> letterCombinations (const string &digits) {
vector<string> result;
if (digits.empty()) return result;
dfs(digits, 0, "", result);
return result;
}
void dfs(const string &digits, size_t cur, string path,
vector<string> &result) {
if (cur == digits.size()) {
result.push_back(path);
return;
}
for (auto c : keyboard[digits[cur] - '0']) {
dfs(digits, cur + 1, path + c, result);
}

![Leetcode-CPP 第154页插图](../assets/images/Leetcode-CPP_p154_1_73456677.png)

---

8.6
Letter Combinations of a Phone Number
149
}
};
8.6.2
䔜В
// LeetCode, Letter Combinations of a Phone Number
// ᬥ䬣฼ᱱᏕO(3^n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
const vector<string> keyboard { " ", "", "abc", "def", // '0','1','2',...
"ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
vector<string> letterCombinations (const string &digits) {
if (digits.empty()) return vector<string>();
vector<string> result(1, "");
for (auto d : digits) {
const size_t n = result.size();
const size_t m = keyboard[d - '0'].size();
result.resize(n * m);
for (size_t i = 0; i < m; ++i)
copy(result.begin(), result.begin() + n, result.begin() + n * i);
for (size_t i = 0; i < m; ++i) {
auto begin = result.begin();
for_each(begin + n * i, begin + n * (i+1), [&](string &s) {
s += keyboard[d - '0'][i];
});
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

せ9 』
ᎮᏕчٷ᥋㉑
ᒂ题Ⱍⰺ̼ܩЪ҄㻳ᒺ喌ᬑ̼㘬⩗ܵ⇪喌䉙ᓲ喌Ύ̼㘬⩗ߗ㻳ᬥ喌䔈ᬥՈ̶㘬᫨∄āā᥋㉑喌ᅠ
≭̹⩗౩εȡ᥋㉑ܵͩᎮ᥋঻⌠᥋喌Ꭾ᥋䛻䲑ࣷ᰸ᮝ䕉Ꭾ᥋喌ࣻीᎮ᥋喌A* ᥋㉑へȡ⌠᥋䛻䲑ࣷ᰸
ᮝ䕉⌠᥋喌఍⏞∄へȡ
Ꭾ᥋঻⌠᥋䲍፧ㆪѫ喈䮓ε౗មᆄ㞱◨䔈䘗̼̯ܵᵦ喉喌λ㔴᰸Ⱗऻ⮳ᵵ᳥喌ັ҄㶗⹩⟥ᔰ喟ັ
҄មᆄ⟥ᔰ喟ັ҄ݓ䛼喟ᅓڥ᭞ݓ䛼喌解ۢε䔈͙䬝题喌ഩᱛ̹᪣͙䬝题ᅠ解ۢεȡ
9.1
Word Ladder
᣾䔟
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence
from start to end, such that:
• Only one letter can be changed at a time
• Each intermediate word must exist in the dictionary
For example, Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
Note:
• Return 0 if there is no such transformation sequence.
• All words have the same length.
• All words contain only lowercase alphabetic characters.
ܵᲿ
ⅱᰯⴜ䌞ᒳ喌⩗Ꭾ᥋ȡ
150

---

9.1
Word Ladder
151
ࢄ䭎݆
//LeetCode, Word Ladder
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
struct state_t {
string word;
int level;
state_t() { word = ""; level = 0; }
state_t(const string& word, int level) {
this->word = word;
this->level = level;
}
bool operator==(const state_t &other) const {
return this->word == other.word;
}
};
namespace std {
template<> struct hash<state_t> {
public:
size_t operator()(const state_t& s) const {
return str_hash(s.word);
}
private:
std::hash<std::string> str_hash;
};
}
class Solution {
public:
int ladderLength(const string& start, const string &end,
const unordered_set<string> &dict) {
queue<state_t> q;
unordered_set<state_t> visited;
// ݓ䛼
auto state_is_valid = [&](const state_t& s) {
return dict.find(s.word) != dict.end() || s.word == end;
};
auto state_is_target = [&](const state_t &s) {return s.word == end; };
auto state_extend = [&](const state_t &s) {
unordered_set<state_t> result;
for (size_t i = 0; i < s.word.size(); ++i) {
state_t new_state(s.word, s.level + 1);
for (char c = 'a'; c <= 'z'; c++) {
// 䭡ₑऻႆ⃼ᰮᢑ
if (c == new_state.word[i]) continue;
swap(c, new_state.word[i]);

---

152
せ9 』
ᎮᏕчٷ᥋㉑
if (state_is_valid(new_state) &&
visited.find(new_state) == visited.end()) {
result.insert(new_state);
}
swap(c, new_state.word[i]); // ᖑ฼䄔ࢄ䃼
}
}
return result;
};
state_t start_state(start, 0);
q.push(start_state);
visited.insert(start_state);
while (!q.empty()) {
// ࡲ̶̼㘬⩗const auto&喌pop() щݏ䮓ٲ㉏喌
// ᑄ⩗ᅠइ᜿εᗛ⾩ᑄ⩗
const auto state = q.front();
q.pop();
if (state_is_target(state)) {
return state.level + 1;
}
const auto& new_states = state_extend(state);
for (const auto& new_state : new_states) {
q.push(new_state);
visited.insert(new_state);
}
}
return 0;
}
};
ࣻ䭎݆
//LeetCode, Word Ladder
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int ladderLength(const string& start, const string &end,
const unordered_set<string> &dict) {
queue<string> current, next;
// ᒂݼᅱ喌̺̯ᅱ
unordered_set<string> visited;
// ݓ䛼
int level = -1;
// ᅱ⁐
auto state_is_valid = [&](const string& s) {
return dict.find(s) != dict.end() || s == end;
};
auto state_is_target = [&](const string &s) {return s == end;};
auto state_extend = [&](const string &s) {
unordered_set<string> result;

---

9.1
Word Ladder
153
for (size_t i = 0; i < s.size(); ++i) {
string new_word(s);
for (char c = 'a'; c <= 'z'; c++) {
// 䭡ₑऻႆ⃼ᰮᢑ
if (c == new_word[i]) continue;
swap(c, new_word[i]);
if (state_is_valid(new_word) &&
visited.find(new_word) == visited.end()) {
result.insert(new_word);
}
swap(c, new_word[i]); // ᖑ฼䄔ࢄ䃼
}
}
return result;
};
current.push(start);
visited.insert(start);
while (!current.empty()) {
++level;
while (!current.empty()) {
// ࡲ̶̼㘬⩗const auto&喌pop() щݏ䮓ٲ㉏喌
// ᑄ⩗ᅠइ᜿εᗛ⾩ᑄ⩗
const auto state = current.front();
current.pop();
if (state_is_target(state)) {
return level + 1;
}
const auto& new_states = state_extend(state);
for (const auto& new_state : new_states) {
next.push(new_state);
visited.insert(new_state);
}
}
swap(next, current);
}
return 0;
}
};
Ⱗڢ题Ⱍ
• Word Ladder II喌㻰§9.2

---

154
せ9 』
ᎮᏕчٷ᥋㉑
9.2
Word Ladder II
᣾䔟
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start
to end, such that:
• Only one letter can be changed at a time
• Each intermediate word must exist in the dictionary
For example, Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
[
["hit","hot","dot","dog","cog"],
["hit","hot","lot","log","cog"]
]
Note:
• All words have the same length.
• All words contain only lowercase alphabetic characters.
ܵᲿ
䌎Word Ladder ℃喌䔈题᭞ⅱ䌞ᒳᱛ䏚喌̼᭞䌞ᒳ䪮Ꮥ喌Ύ᭞BFS喌⪔ᓝ只☕◨ȡ
ⅱ̯Ა䌞ᒳ঻ⅱᝯ᰸䌞ᒳ᰸ᒷ๖⮳̼ऻ喌ⅱ̯Ა䌞ᒳ喌⃾͙⟥ᔰ㞱◨ङ䰯㺰䃟ᒄ̯͙ݼ侠ࢢञ喛
ⅱᝯ᰸䌞ᒳᬥ喌᰸⮳⟥ᔰ㞱◨ञ㘬᰸้͙❥㞱◨喌ࢢ㺰䃟ᒄ้͙ݼ侠ȡ
ັ᳋ᒂݼ䌞ᒳ䪮Ꮥጡ㏾䊴䓶ᒂݼᰯⴜ䌞ᒳ䪮Ꮥ喌ञД͜ₑᄨ䄔䌞ᒳ⮳ำ⤵喌ఏͩᝀЛ㺰ឭ⮳᭞
ᰯⴜ䌞ᒳȡ
ࢄ䭎݆
//LeetCode, Word Ladder II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
struct state_t {
string word;
int level;
state_t() { word = ""; level = 0; }
state_t(const string& word, int level) {
this->word = word;
this->level = level;
}

---

9.2
Word Ladder II
155
bool operator==(const state_t &other) const {
return this->word == other.word;
}
};
namespace std {
template<> struct hash<state_t> {
public:
size_t operator()(const state_t& s) const {
return str_hash(s.word);
}
private:
std::hash<std::string> str_hash;
};
}
class Solution {
public:
vector<vector<string> > findLadders(const string& start,
const string& end, const unordered_set<string> &dict) {
queue<state_t> q;
unordered_set<state_t> visited; // ݓ䛼
unordered_map<state_t, vector<state_t> > father; // DAG
auto state_is_valid = [&](const state_t& s) {
return dict.find(s.word) != dict.end() || s.word == end;
};
auto state_is_target = [&](const state_t &s) {return s.word == end; };
auto state_extend = [&](const state_t &s) {
unordered_set<state_t> result;
for (size_t i = 0; i < s.word.size(); ++i) {
state_t new_state(s.word, s.level + 1);
for (char c = 'a'; c <= 'z'; c++) {
// 䭡ₑऻႆ⃼ᰮᢑ
if (c == new_state.word[i]) continue;
swap(c, new_state.word[i]);
if (state_is_valid(new_state)) {
auto visited_iter = visited.find(new_state);
if (visited_iter != visited.end()) {
if (visited_iter->level < new_state.level) {
// do nothing
} else if (visited_iter->level == new_state.level) {
result.insert(new_state);
} else { // not possible
throw std::logic_error("not possible to get here");
}
} else {
result.insert(new_state);

---

156
せ9 』
ᎮᏕчٷ᥋㉑
}
}
swap(c, new_state.word[i]); // ᖑ฼䄔ࢄ䃼
}
}
return result;
};
vector<vector<string>> result;
state_t start_state(start, 0);
q.push(start_state);
visited.insert(start_state);
while (!q.empty()) {
// ࡲ̶̼㘬⩗const auto&喌pop() щݏ䮓ٲ㉏喌
// ᑄ⩗ᅠइ᜿εᗛ⾩ᑄ⩗
const auto state = q.front();
q.pop();
// ັ᳋ᒂݼ䌞ᒳ䪮Ꮥጡ㏾䊴䓶ᒂݼᰯⴜ䌞ᒳ䪮Ꮥ喌
// ञД͜ₑᄨ䄔䌞ᒳ⮳ำ⤵喌ఏͩᝀЛ㺰ឭ⮳᭞ᰯⴜ䌞ᒳ
if (!result.empty() && state.level + 1 > result[0].size()) break;
if (state_is_target(state)) {
vector<string> path;
gen_path(father, start_state, state, path, result);
continue;
}
// ᓴ䶪ᡙݟ̺䲑喌℃ັऻ̯ᅱA ঻B ͓͙㞱◨౶ᠶीεⰝᴶ㞱◨喌
// 䗒ͷⰝᴶ㞱◨ᅠщ౗q ͜ܩ⣟͓⁐喌䓂ܩ䌞ᒳᅠщ㔪Լ
// visited.insert(state);
// មᆄ㞱◨
const auto& new_states = state_extend(state);
for (const auto& new_state : new_states) {
if (visited.find(new_state) == visited.end()) {
q.push(new_state);
}
visited.insert(new_state);
father[new_state].push_back(state);
}
}
return result;
}
private:
void gen_path(unordered_map<state_t, vector<state_t> > &father,
const state_t &start, const state_t &state, vector<string> &path,
vector<vector<string> > &result) {
path.push_back(state.word);
if (state == start) {
if (!result.empty()) {
if (path.size() < result[0].size()) {

---

9.2
Word Ladder II
157
result.clear();
result.push_back(path);
reverse(result.back().begin(), result.back().end());
} else if (path.size() == result[0].size()) {
result.push_back(path);
reverse(result.back().begin(), result.back().end());
} else { // not possible
throw std::logic_error("not possible to get here ");
}
} else {
result.push_back(path);
reverse(result.back().begin(), result.back().end());
}
} else {
for (const auto& f : father[state]) {
gen_path(father, start, f, path, result);
}
}
path.pop_back();
}
};
ࣻ䭎݆
//LeetCode, Word Ladder II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<string> > findLadders(const string& start,
const string& end, const unordered_set<string> &dict) {
// ᒂݼᅱ喌̺̯ᅱ喌⩗unordered_set ᭞ͩε࣪䛼喌Һັ͓͙❥㞱◨ᠶी
// ऻ̯͙ၿ㞱◨喌ັ᳋⩗vector, ၿ㞱◨ᅠщ౗next 䛻ܩ⣟͓⁐喌ڥჍₓ
// ᬥfather ጡ㏾䃟ᒄε͓͙❥㞱◨喌next 䛻䛼฼ܩ⣟͓⁐᭞⇐ᓴ㺰⮳
unordered_set<string> current, next;
unordered_set<string> visited; // ݓ䛼
unordered_map<string, vector<string> > father; // DAG
int level = -1;
// ᅱ⁐
auto state_is_valid = [&](const string& s) {
return dict.find(s) != dict.end() || s == end;
};
auto state_is_target = [&](const string &s) {return s == end;};
auto state_extend = [&](const string &s) {
unordered_set<string> result;
for (size_t i = 0; i < s.size(); ++i) {
string new_word(s);
for (char c = 'a'; c <= 'z'; c++) {
// 䭡ₑऻႆ⃼ᰮᢑ
if (c == new_word[i]) continue;

---

158
せ9 』
ᎮᏕчٷ᥋㉑
swap(c, new_word[i]);
if (state_is_valid(new_word) &&
visited.find(new_word) == visited.end()) {
result.insert(new_word);
}
swap(c, new_word[i]); // ᖑ฼䄔ࢄ䃼
}
}
return result;
};
vector<vector<string> > result;
current.insert(start);
while (!current.empty()) {
++ level;
// ັ᳋ᒂݼ䌞ᒳ䪮Ꮥጡ㏾䊴䓶ᒂݼᰯⴜ䌞ᒳ䪮Ꮥ喌ञД͜ₑᄨ䄔䌞ᒳ⮳
// ำ⤵喌ఏͩᝀЛ㺰ឭ⮳᭞ᰯⴜ䌞ᒳ
if (!result.empty() && level+1 > result[0].size()) break;
// 1. ᐥ䔎ߏڔ visited, 䔈ᵦ᝼㘬ٰ䃧͓͙❥㞱◨ᠶीऻ̯͙ၿ㞱◨
// 2. ̯㗐㙀current ڗ䘗ߏڔ visited, ᭞䭡ₑᱛᅱݼ̯͙㞱◨មᆄ
// 㞱◨ᬥ喌ᠶीεᱛᅱऽ䲑ᅉ᱙ำ⤵⮳㞱◨喌䔈Ა䌞ᒳᓴ♥̼᭞ᰯⴜ⮳
for (const auto& state : current)
visited.insert(state);
for (const auto& state : current) {
if (state_is_target(state)) {
vector<string> path;
gen_path(father, path, start, state, result);
continue;
}
const auto new_states = state_extend(state);
for (const auto& new_state : new_states) {
next.insert(new_state);
father[new_state].push_back(state);
}
}
current.clear();
swap(current, next);
}
return result;
}
private:
void gen_path(unordered_map<string, vector<string> > &father,
vector<string> &path, const string &start, const string &word,
vector<vector<string> > &result) {
path.push_back(word);
if (word == start) {
if (!result.empty()) {

---

9.2
Word Ladder II
159
if (path.size() < result[0].size()) {
result.clear();
result.push_back(path);
} else if(path.size() == result[0].size()) {
result.push_back(path);
} else {
// not possible
throw std::logic_error("not possible to get here");
}
} else {
result.push_back(path);
}
reverse(result.back().begin(), result.back().end());
} else {
for (const auto& f : father[word]) {
gen_path(father, path, start, f, result);
}
}
path.pop_back();
}
};
భ⮳Ꭾ᥋
ᱛ题䔇ञДⰺ։᭞భ̹⮳Ꭾ᥋ȡ㐈჉εႆڧ dict喌ञДഩνႲ⩪ܩ̯͙ᬏीభ喌㶗⹩ࢄ䃼ͺ䬣
ञДρⰧ䒛ᢑȡᱛ题⮳ᱛ䉗ᅠ᭞ጡⴔ䊦◨঻㏷◨喌౗భ̹ឭܩᝯ᰸ᰯⴜ䌞ᒳȡ
//LeetCode, Word Ladder II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<string> > findLadders(const string& start,
const string &end, const unordered_set<string> &dict) {
const auto& g = build_graph(dict);
vector<state_t*> pool;
queue<state_t*> q; // ᱙ำ⤵⮳㞱◨
// value ᭞ᝯ౗ᅱ⁐
unordered_map<string, int> visited;
auto state_is_target = [&](const state_t *s) {return s->word == end; };
vector<vector<string>> result;
q.push(create_state(nullptr, start, 0, pool));
while (!q.empty()) {
state_t* state = q.front();
q.pop();
// ັ᳋ᒂݼ䌞ᒳ䪮Ꮥጡ㏾䊴䓶ᒂݼᰯⴜ䌞ᒳ䪮Ꮥ喌
// ञД͜ₑᄨ䄔䌞ᒳ⮳ำ⤵喌ఏͩᝀЛ㺰ឭ⮳᭞ᰯⴜ䌞ᒳ
if (!result.empty() && state->level+1 > result[0].size()) break;
if (state_is_target(state)) {

---

160
せ9 』
ᎮᏕчٷ᥋㉑
const auto& path = gen_path(state);
if (result.empty()) {
result.push_back(path);
} else {
if (path.size() < result[0].size()) {
result.clear();
result.push_back(path);
} else if (path.size() == result[0].size()) {
result.push_back(path);
} else {
// not possible
throw std::logic_error("not possible to get here");
}
}
continue;
}
visited[state->word] = state->level;
// មᆄ㞱◨
auto iter = g.find(state->word);
if (iter == g.end()) continue;
for (const auto& neighbor : iter->second) {
auto visited_iter = visited.find(neighbor);
if (visited_iter != visited.end() &&
visited_iter->second < state->level + 1) {
continue;
}
q.push(create_state(state, neighbor, state->level + 1, pool));
}
}
// release all states
for (auto state : pool) {
delete state;
}
return result;
}
private:
struct state_t {
state_t* father;
string word;
int level; // ᝯ౗ᅱ⁐喌Ͻ 0 ᐯ໺㑅द
state_t(state_t* father_, const string& word_, int level_) :
father(father_), word(word_), level(level_) {}
};
state_t* create_state(state_t* parent, const string& value,
int length, vector<state_t*>& pool) {

---

9.2
Word Ladder II
161
state_t* node = new state_t(parent, value, length);
pool.push_back(node);
return node;
}
vector<string> gen_path(const state_t* node) {
vector<string> path;
while(node != nullptr) {
path.push_back(node->word);
node = node->father;
}
reverse(path.begin(), path.end());
return path;
}
unordered_map<string, unordered_set<string> > build_graph(
const unordered_set<string>& dict) {
unordered_map<string, unordered_set<string> > adjacency_list;
for (const auto& word : dict) {
for (size_t i = 0; i < word.size(); ++i) {
string new_word(word);
for (char c = 'a'; c <= 'z'; c++) {
// 䭡ₑऻႆ⃼ᰮᢑ
if (c == new_word[i]) continue;
swap(c, new_word[i]);
if ((dict.find(new_word) != dict.end())) {
auto iter = adjacency_list.find(word);
if (iter != adjacency_list.end()) {
iter->second.insert(new_word);
} else {
adjacency_list.insert(pair<string,
unordered_set<string>>(word, unordered_set<string>()));
adjacency_list[word].insert(new_word);
}
}
swap(c, new_word[i]); // ᖑ฼䄔ࢄ䃼
}
}
}
return adjacency_list;
}
};
Ⱗڢ题Ⱍ
• Word Ladder喌㻰§9.1

---

162
せ9 』
ᎮᏕчٷ᥋㉑
9.3
Surrounded Regions
᣾䔟
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region .
For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
ܵᲿ
Ꭾ᥋ȡϽ̹̺ጕढఊ͙䓨⩻ᒯ䛻䊟喌ܐ᭞㘬⷟ݟ⮳'O'喌䘬᭞䌎䓨⩻ᣔณ⮳喌Ꮓ䄔Ԍ⪈ȡ
Вⴰ
// LeetCode, Surrounded Regions
// BFS喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
void solve(vector<vector<char>> &board) {
if (board.empty()) return;
const int m = board.size();
const int n = board[0].size();
for (int i = 0; i < n; i++) {
bfs(board, 0, i);
bfs(board, m - 1, i);
}
for (int j = 1; j < m - 1; j++) {
bfs(board, j, 0);
bfs(board, j, n - 1);
}
for (int i = 0; i < m; i++)
for (int j = 0; j < n; j++)
if (board[i][j] == 'O')
board[i][j] = 'X';
else if (board[i][j] == '+')
board[i][j] = 'O';
}
private:
void bfs(vector<vector<char>> &board, int i, int j) {

---

9.3
Surrounded Regions
163
typedef pair<int, int> state_t;
queue<state_t> q;
const int m = board.size();
const int n = board[0].size();
auto state_is_valid = [&](const state_t &s) {
const int x = s.first;
const int y = s.second;
if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] != 'O')
return false;
return true;
};
auto state_extend = [&](const state_t &s) {
vector<state_t> result;
const int x = s.first;
const int y = s.second;
// ̹̺ጕढ
const state_t new_states[4] = {{x-1,y}, {x+1,y},
{x,y-1}, {x,y+1}};
for (int k = 0; k < 4;
++k) {
if (state_is_valid(new_states[k])) {
// ᬑ᰸ᴶ䃟ߎ㘬ࣷ᰸࣪䛼ߎ㘬
board[new_states[k].first][new_states[k].second] = '+';
result.push_back(new_states[k]);
}
}
return result;
};
state_t start = { i, j };
if (state_is_valid(start)) {
board[i][j] = '+';
q.push(start);
}
while (!q.empty()) {
auto cur = q.front();
q.pop();
auto new_states = state_extend(cur);
for (auto s : new_states) q.push(s);
}
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

164
せ9 』
ᎮᏕчٷ᥋㉑
9.4
ᄾ㐂
9.4.1
䔱⩗౩ᮞ
䓂ڔ᪟ᢝ喚⇐ϯͷ➨ᒰ喌̼׾⌠᥋喌䰯㺰᰸Ć䕁ᒁć⮳ᕖ䉗ȡັ᳋᭞ᵀᝅ㔴భ喌ằ⢶ᰣ๖ȡ
⟥ᔰ䒛ᢑభ喚ᵀᝅ㔴DAG భȡ
ⅱ解Ⱍᴶ喚ⅱᰯⴜȡ
9.4.2
ᕌ㔲⮳ₔ俓
1. ᭞ⅱ䌞ᒳ䪮Ꮥ喌䔇᭞䌞ᒳᱛ䏚喈ᝅߗҋᎾ݆喉喟
(a) ັ᳋᭞ⅱ䌞ᒳ䪮Ꮥ喌݈⟥ᔰ䛻䲑㺰ႇ䌞ᒳ䪮Ꮥ喈ᝅࣻ䭎݆+ ̯͙ڗᅯइ䛾喉
(b) ັ᳋᭞ⅱ䌞ᒳᱛ䏚ᝅߗҋᎾ݆
i. 㺰⩗̯Ḥᵀႇחწ᥋䓶⼺͜⮳䌞ᒳ
ii. ᭞ॕञД䶳џ⟥ᔰ͙᪟⮳̹䭿喟㘬๎䶳џ⟥ᔰᕪ᪟喌݈ᐯ̯͙๖᪟㏳喌⩗ᵀ⮳ࣻϡ
㶗⹩∄喛ັ᳋̼㘬䶳џ⟥ᔰᕪ᪟喌݈㺰Ү⩗̯Ḥ䕉⩗⮳ᵀȡ䔈̯ₔΎ᭞せ4 ₔ⮳ᓴ
㺰̼ٴܵᲐХȡ
2. ັ҄㶗⹩⟥ᔰ喟ࢢ̯͙⟥ᔰ䰯㺰ႇחਙϊϊᓴ㺰⮳᪟ᢝ喌᝼㘬๎Ⴛ᪣᣿ӊັ҄មᆄݟ̺̯ₔ
⟥ᔰ⮳ᝯ᰸Ԑᖞȡ̯㝛䃟ᒄᒂݼѼ㒝ᝅ᪣҂ᅯ䲑ȡ
3. ັ҄មᆄ⟥ᔰ喟䔈̯ₔ䌎せ2 ₔⰧڢȡ⟥ᔰ䛻䃟ᒄ⮳᪟ᢝ̼ऻ喌មᆄ᫨∄ᅠ̼ऻȡᄨν఩჉̼
इ⮳᪟ᢝ㐂Ჳ喈̯㝛题ⰝⰣᣔ㐈ܩ喌ҋͩ䓂ڔ᪟ᢝ喉喌ັλࣸᵀ喌భへ喌មᆄ᫨∄ᒷクࢄ喌Ⱓ
ᣔᒯ̺̯ᅱ䊟喌ᄨν䮿ᐾభ喌㺰ٷ౗せ1 ₔ䛻ᘢ⌴ẉ⟥ᔰᝯፕ⮳᪟ᢝ喌ᘢ⌴ẉε䔈◨喌䗒ັ҄
មᆄᅠᒷクࢄεȡ
4. ັ҄ݓ᫜䛼฼喟ັ᳋⟥ᔰ䒛ᢑభ᭞̯䷆ᵀ喌݈Ⅷ䔋̼щܩ⣟఍䌞喌̼䰯㺰ݓ䛼喛ັ᳋⟥ᔰ䒛ᢑ
భ᭞̯͙భ喈䔈ᬥՈ᭞̯͙భ̹⮳BFS喉喌݈䰯㺰ݓ䛼ȡ
(a) ັ᳋᭞ⅱᰯⴜ䌞ᒳ䪮Ꮥᝅ̯Ა䌞ᒳ喌݈ङ䰯㺰䃘Ć◨ć喈ࢢ⟥ᔰ喉̼䛼฼ܩ⣟喌ࢢञԌ䃰
̼ܩ⣟఍䌞
(b) ັ᳋᭞ⅱᝯ᰸䌞ᒳ喌∗ᘾₓᬥ喌⟥ᔰ䒛ᢑభ᭞DAG喌ࢢٰ䃧͓͙❥㞱◨ᠶीऻ̯͙ၿ㞱
◨ȡڦ҂Ⴭ⣟ᬥ喌⃾͙㞱◨㺰Ćᐥ䔎ćߏڔݟጡ䃮䬝䯵षvisited喌㺰へ̯ᅱڗ䘗䃮䬝
Ⴛऽ喌ڼߏڔݟvisited 䯵षȡ
(c) ڦ҂Ⴭ⣟
i. ⟥ᔰ᭞ॕႇ౗Ⴛ㒽৷ጻ᫨ᵷ喟ࢢᄵ⟥ᔰ̯̯᭏ᄳݟ᪣᪟喌ρⰧͺ䬣̼щۡ⾰ȡ
ii. ັ᳋̼ႇ౗喌݈䰯㺰Ү⩗䕉⩗⮳৷ጻ㶗喈㜙ጠჍ⣟ᝅ⩗ᴶ۵Ꮒ喌Һັunordered_-
set喉Ეݓ䛼喛㜙ጠჍ⣟৷ጻ㶗⮳䄌喌ັ᳋㘬๎䶳џ⟥ᔰ͙᪟⮳̹䭿喌݈ञДᐯ͓͙
᪟㏳喌head ঻next喌㶗⹩৷ጻ㶗喌ࣱ㔲せ§??㞱᫨ᵷ2ȡ

---

9.4
ᄾ㐂
165
iii. ັ᳋ႇ౗喌݈ञДᐯ̯͙๖ጲᅃ᪟㏳喌Ეݓ䛼喌̓ₓᬥञД㇭⶝䃐テܩ⟥ᔰᕪ᪟喌㔻
̼ϴϴ᭞䶳џ̹䭿ȡ
5. Ⱍᴶ⟥ᔰ᭞ॕጡⴔ喟ັ᳋题Ⱍጡ㏾㐈ܩεⰝᴶ⟥ᔰ喌ञДፕᲔᒷ๖Ӯݘ喌䔈ᬥՈञДϽ䊦໺⟥
ᔰܩऀ喌ₒीᎮ᥋喛ΎञДϽⰝᴶ⟥ᔰܩऀ喌䔵ीᎮ᥋喛ΎञДऻᬥܩऀ喌ࣻीᎮ᥋ȡ
9.4.3
ВⴰὐᲮ
Ꭾ᥋䰯㺰̯͙䭎݆喌⩗ν̯ᅱ̯ᅱមᆄ喌̯͙ hashset喌⩗νݓ䛼喌̯Ḥᵀ喈ङⅱ䪮Ꮥᬥ̼䰯㺰喉喌
⩗νႇח᪣Ḥᵀȡ
ᄨν䭎݆喌ञД⩗queue喌ΎञДឹvector ᒂ։䭎݆Ү⩗ȡᒂⅱ䪮Ꮥᬥ喌᰸͓⻼։∄喚
1. ङ⩗̯͙䭎݆喌ѵ౗⟥ᔰ㐂Ჳ҂ state_t 䛻෍ߏ̯͙᪣᪟ႆ⃤level喌㶗⹩ᒂݼᝯ౗⮳ᅱ⁐喌
ᒂ⷟ݟⰝᴶ⟥ᔰ喌Ⱓᣔ䓂ܩlevel ࢢञȡ䔈͙᫨ᵷ喌ञДᒷშᭂ⮳इ᜿A* テ∄喌ឹqueue
ᰮᢑͩ priority_queue ࢢञȡ
2. ⩗͓͙䭎݆喌current, next喌ܵݚ㶗⹩ᒂݼᅱ⁐঻̺̯ᅱ喌क䃭̯͙ڗᅯ᪣᪟level喌㶗⹩
ᅱ᪟喈Ύࢢ䌞ᒳ䪮Ꮥ喉喌ᒂ⷟ݟⰝᴶ⟥ᔰ喌䓂ܩlevel ࢢञȡ䔈͙᫨ᵷ喌⟥ᔰ䛻ञД̼ႇ䌞ᒳ
䪮Ꮥ喌ङ䰯ڗᅯ䃭㒝̯͙᪣᪟level喌℃䒲㞱ⰰڴႇ喛
ᄨν hashset喌ັ᳋᰸Ⴛ㒽৷ጻ᫨ᵷ喌⩗ጲᅃ᪟㏳(bool visited[STATE_MAX] ᝅvector<bool>
visited(STATE_MAX, false)) Ე㶗⹩喛ັ᳋⇐᰸喌ञД⩗STL 䛻⮳set ᝅunordered_setȡ
ᄨνᵀ喌ັ᳋⩗STL喌ञД⩗unordered_map<state_t, state_t > father 㶗⹩̯䷆ᵀ喌Вⴰ䲍
፧ク∰ȡັ᳋㘬๎䶳џ⟥ᔰᕪ᪟⮳̹䭿喈䃭ͩ STATE_MAX喉喌ञД⩗᪟㏳(state_t nodes[STATE_-
MAX])喌ࢢᵀ⮳ࣻϡ㶗⹩∄Ე㶗⹩ᵀ喌᩷⢶ᰣ倇喌ᒂ♥喌䰯㺰ۈᰣ้Вⴰȡ
ັ҄㶗⹩⟥ᔰ
bfs_common.h
/** ⟥ᔰ*/
struct state_t {
int data1;
/** ⟥ᔰ⮳᪟ᢝ喌ञД᰸้͙ႆ⃤. */
int data2;
/** ⟥ᔰ⮳᪟ᢝ喌ञД᰸้͙ႆ⃤. */
// dataN;
/** ڥЅႆ⃤*/
int action; /** ⩠❥⟥ᔰ⼪ߗݟᱛ⟥ᔰ⮳ߗҋ喌ⅱߗҋᎾ݆ᬥ䰯㺰. */
int level;
/** ᝯ౗⮳ᅱ⁐喈Ͻ 0 ᐯ໺喉喌Ύࢢ䌞ᒳ䪮Ꮥ-1喌ⅱ䌞ᒳ䪮Ꮥᬥ䰯㺰喛
̼䓶喌䛶⩗ࣻ䭎݆ᬥ̼䰯㺰ᱛႆ⃤喌ङ䰯ڗᅯ䃭̯͙᪣᪟*/
bool operator==(const state_t &other) const {
return true;
// ᵨᢝڦ҂䬝题Ⴭ⣟
}
};
// ჉͸ hash ܬ᪟
// ᫨∄1喚ὐᲮ➨ࡅ喌ᒂhash ܬ᪟ङ䰯㺰⟥ᔰᱛ䏚喌̼䰯㺰ڥЅ᪟ᢝᬥ喌⩗䔈͙᫨∄℃䒲ク∰
namespace std {
template<> struct hash<state_t> {

---

166
せ9 』
ᎮᏕчٷ᥋㉑
size_t operator()(const state_t & x) const {
return 0; // ᵨᢝڦ҂䬝题Ⴭ⣟
}
};
}
// ᫨∄2喚ܬ᪟ᄨ䆐喌ັ᳋hash ܬ᪟䰯㺰䓿㵻ᬥ᪟ᢝ喌݈⩗䔈⻼᫨∄
class Hasher {
public:
Hasher(int _m) : m(_m) {};
size_t operator()(const state_t &s) const {
return 0; // ᵨᢝڦ҂䬝题Ⴭ⣟
}
private:
int m; // ႇᩭๅ䲑яڔ⮳᪟ᢝ
};
/**
* @brief ࣼी⩎᜿䌞ᒳ喌ⅱ̯Ა䌞ᒳ.
* @param[in] father ᵀ
* @param[in] target Ⱍᴶ㞱◨
* @return Ͻ䊦◨ݟtarget ⮳䌞ᒳ
*/
vector<state_t> gen_path(const unordered_map<state_t, state_t> &father,
const state_t &target) {
vector<state_t> path;
path.push_back(target);
for (state_t cur = target; father.find(cur) != father.end();
cur = father.at(cur))
path.push_back(cur);
reverse(path.begin(), path.end());
return path;
}
/**
* ࣼी⩎᜿䌞ᒳ喌ⅱᝯ᰸䌞ᒳ.
* @param[in] father ႇᩭεᝯ᰸䌞ᒳ⮳ᵀ
* @param[in] start 䊦◨
* @param[in] state ㏷◨
* @return Ͻ䊦◨ݟ㏷◨⮳ᝯ᰸䌞ᒳ
*/
void gen_path(unordered_map<state_t, vector<state_t> > &father,
const string &start, const state_t& state, vector<state_t> &path,
vector<vector<state_t> > &result) {
path.push_back(state);
if (state == start) {
if (!result.empty()) {
if (path.size() < result[0].size()) {
result.clear();
result.push_back(path);

---

9.4
ᄾ㐂
167
} else if(path.size() == result[0].size()) {
result.push_back(path);
} else {
// not possible
throw std::logic_error("not possible to get here");
}
} else {
result.push_back(path);
}
reverse(result.back().begin(), result.back().end());
} else {
for (const auto& f : father[state]) {
gen_path(father, start, f, path, result);
}
}
path.pop_back();
}
bfs_common.h
ⅱᰯⴜ䌞ᒳ䪮Ꮥᝅ̯Ა䌞ᒳ
ࢄ䭎݆⮳ۈ∄
bfs_template.cpp
#include "bfs_common.h"
/**
* @brief Ꭾ᥋喌ङ⩗̯͙䭎݆.
* @param[in] start 䊦◨
* @param[in] data 䓂ڔ᪟ᢝ
* @return Ͻ䊦◨ݟⰝᴶ⟥ᔰ⮳̯Აᰯⴜ䌞ᒳ
*/
vector<state_t> bfs(state_t &start, const vector<vector<int>> &grid) {
queue<state_t> q; // 䭎݆
unordered_set<state_t> visited; // ݓ䛼
unordered_map<state_t, state_t> father; // ᵀ喌ⅱ䌞ᒳᱛ䏚ᬥ᝼䰯㺰
// ݓ᫜⟥ᔰ᭞ॕष∄
auto state_is_valid = [&](const state_t &s) { /*...*/ };
// ݓ᫜ᒂݼ⟥ᔰ᭞ॕͩᝯⅱⰝᴶ
auto state_is_target = [&](const state_t &s) { /*...*/ };
// មᆄᒂݼ⟥ᔰ
auto state_extend = [&](const state_t &s) {
unordered_set<state_t> result;
for (/*...*/) {
const state_t new_state = /*...*/;
if (state_is_valid(new_state) &&
visited.find(new_state) != visited.end()) {
result.insert(new_state);
}
}

---

168
せ9 』
ᎮᏕчٷ᥋㉑
return result;
};
assert (start.level == 0);
q.push(start);
while (!q.empty()) {
// ࡲ̶̼㘬⩗const auto&喌pop() щݏ䮓ٲ㉏喌
// ᑄ⩗ᅠइ᜿εᗛ⾩ᑄ⩗
const state_t state = q.front();
q.pop();
visited.insert(state);
// 䃮䬝㞱◨
if (state_is_target(state)) {
return return gen_path(father, target); // ⅱ̯Ა䌞ᒳ
// return state.level + 1; // ⅱ䌞ᒳ䪮Ꮥ
}
// មᆄ㞱◨
vector<state_t> new_states = state_extend(state);
for (const auto& new_state : new_states) {
q.push(new_state);
father[new_state] = state;
// ⅱ̯Ა䌞ᒳ
// visited.insert(state); // чࡅ喚ञД᣿ݼߏڔ visited 䯵ष喌
// Ͻ㔻㑘ᄾ⟥ᔰមᆄȡ䔈ᬥq ⮳ग़͸⪔᰸इࡅ喌䛻䲑ႇᩭ⮳᭞ำ⤵ε̯ࡹ
// ⮳㞱◨喚ጡ㏾ߏڔε visited喌ѵ䔇⇐᰸មᆄȡݚᔇ䃟while ᓙ⣞ᐯ໺
// ݼ喌㺰ߏ̯㵻Вⴰ, visited.insert(start)
}
}
return vector<state_t>();
//return 0;
}
bfs_template.cpp
ࣻ䭎݆⮳ۈ∄
bfs_template1.cpp
#include "bfs_common.h"
/**
* @brief Ꭾ᥋喌Ү⩗͓͙䭎݆.
* @param[in] start 䊦◨
* @param[in] data 䓂ڔ᪟ᢝ
* @return Ͻ䊦◨ݟⰝᴶ⟥ᔰ⮳̯Აᰯⴜ䌞ᒳ
*/
vector<state_t> bfs(const state_t &start, const type& data) {
queue<state_t> next, current; // ᒂݼᅱ喌̺̯ᅱ
unordered_set<state_t> visited; // ݓ䛼
unordered_map<state_t, state_t> father; // ᵀ喌ⅱ䌞ᒳᱛ䏚ᬥ᝼䰯㺰
int level = -1;
// ᅱ⁐
// ݓ᫜⟥ᔰ᭞ॕष∄

---

9.4
ᄾ㐂
169
auto state_is_valid = [&](const state_t &s) { /*...*/ };
// ݓ᫜ᒂݼ⟥ᔰ᭞ॕͩᝯⅱⰝᴶ
auto state_is_target = [&](const state_t &s) { /*...*/ };
// មᆄᒂݼ⟥ᔰ
auto state_extend = [&](const state_t &s) {
unordered_set<state_t> result;
for (/*...*/) {
const state_t new_state = /*...*/;
if (state_is_valid(new_state) &&
visited.find(new_state) != visited.end()) {
result.insert(new_state);
}
}
return result;
};
current.push(start);
while (!current.empty()) {
++level;
while (!current.empty()) {
// ࡲ̶̼㘬⩗const auto&喌pop() щݏ䮓ٲ㉏喌
// ᑄ⩗ᅠइ᜿εᗛ⾩ᑄ⩗
const auto state = current.front();
current.pop();
visited.insert(state);
if (state_is_target(state)) {
return return gen_path(father, state); // ⅱ̯Ა䌞ᒳ
// return state.level + 1; // ⅱ䌞ᒳ䪮Ꮥ
}
const auto& new_states = state_extend(state);
for (const auto& new_state : new_states) {
next.push(new_state);
father[new_state] = state;
// visited.insert(state); // чࡅ喚ञД᣿ݼߏڔ visited 䯵ष喌
// Ͻ㔻㑘ᄾ⟥ᔰមᆄȡ䔈ᬥcurrent ⮳ग़͸⪔᰸इࡅ喌䛻䲑ႇᩭ⮳᭞ำ
// ⤵ε̯ࡹ⮳㞱◨喚ጡ㏾ߏڔε visited喌ѵ䔇⇐᰸មᆄȡݚᔇ䃟while
// ᓙ⣞ᐯ໺ݼ喌㺰ߏ̯㵻Вⴰ, visited.insert(start)
}
}
swap(next, current); //!!! ϓᢑ͓͙䭎݆
}
return vector<state_t>();
// return 0;
}
bfs_template1.cpp

---

170
せ9 』
ᎮᏕчٷ᥋㉑
ⅱᝯ᰸䌞ᒳ
ࢄ䭎݆
bfs_template.cpp
/**
* @brief Ꭾ᥋喌Ү⩗̯͙䭎݆.
* @param[in] start 䊦◨
* @param[in] data 䓂ڔ᪟ᢝ
* @return Ͻ䊦◨ݟⰝᴶ⟥ᔰ⮳ᝯ᰸ᰯⴜ䌞ᒳ
*/
vector<vector<state_t> > bfs(const state_t &start, const type& data) {
queue<state_t> q;
unordered_set<state_t> visited; // ݓ䛼
unordered_map<state_t, vector<state_t> > father; // DAG
auto state_is_valid = [&](const state_t& s) { /*...*/ };
auto state_is_target = [&](const state_t &s) { /*...*/ };
auto state_extend = [&](const state_t &s) {
unordered_set<state_t> result;
for (/*...*/) {
const state_t new_state = /*...*/;
if (state_is_valid(new_state)) {
auto visited_iter = visited.find(new_state);
if (visited_iter != visited.end()) {
if (visited_iter->level < new_state.level) {
// do nothing
} else if (visited_iter->level == new_state.level) {
result.insert(new_state);
} else { // not possible
throw std::logic_error("not possible to get here");
}
} else {
result.insert(new_state);
}
}
}
return result;
};
vector<vector<string>> result;
state_t start_state(start, 0);
q.push(start_state);
visited.insert(start_state);
while (!q.empty()) {
// ࡲ̶̼㘬⩗const auto&喌pop() щݏ䮓ٲ㉏喌
// ᑄ⩗ᅠइ᜿εᗛ⾩ᑄ⩗
const auto state = q.front();
q.pop();
// ັ᳋ᒂݼ䌞ᒳ䪮Ꮥጡ㏾䊴䓶ᒂݼᰯⴜ䌞ᒳ䪮Ꮥ喌
// ञД͜ₑᄨ䄔䌞ᒳ⮳ำ⤵喌ఏͩᝀЛ㺰ឭ⮳᭞ᰯⴜ䌞ᒳ

---

9.4
ᄾ㐂
171
if (!result.empty() && state.level + 1 > result[0].size()) break;
if (state_is_target(state)) {
vector<string> path;
gen_path(father, start_state, state, path, result);
continue;
}
// ᓴ䶪ᡙݟ̺䲑喌℃ັऻ̯ᅱA ঻B ͓͙㞱◨౶ᠶीεⰝᴶ㞱◨喌
// 䗒ͷⰝᴶ㞱◨ᅠщ౗q ͜ܩ⣟͓⁐喌䓂ܩ䌞ᒳᅠщ㔪Լ
// visited.insert(state);
// មᆄ㞱◨
const auto& new_states = state_extend(state);
for (const auto& new_state : new_states) {
if (visited.find(new_state) == visited.end()) {
q.push(new_state);
}
visited.insert(new_state);
father[new_state].push_back(state);
}
}
return result;
}
bfs_template.cpp
ࣻ䭎݆⮳ۈ∄
bfs_template.cpp
#include "bfs_common.h"
/**
* @brief Ꭾ᥋喌Ү⩗͓͙䭎݆.
* @param[in] start 䊦◨
* @param[in] data 䓂ڔ᪟ᢝ
* @return Ͻ䊦◨ݟⰝᴶ⟥ᔰ⮳ᝯ᰸ᰯⴜ䌞ᒳ
*/
vector<vector<state_t> > bfs(const state_t &start, const type& data) {
// ᒂݼᅱ喌̺̯ᅱ喌⩗unordered_set ᭞ͩε࣪䛼喌Һັ͓͙❥㞱◨ᠶी
// ऻ̯͙ၿ㞱◨喌ັ᳋⩗vector, ၿ㞱◨ᅠщ౗next 䛻ܩ⣟͓⁐喌ڥჍₓ
// ᬥfather ጡ㏾䃟ᒄε͓͙❥㞱◨喌next 䛻䛼฼ܩ⣟͓⁐᭞⇐ᓴ㺰⮳
unordered_set<string> current, next;
unordered_set<state_t> visited; // ݓ䛼
unordered_map<state_t, vector<state_t> > father; // DAG
int level = -1;
// ᅱ⁐
// ݓ᫜⟥ᔰ᭞ॕष∄
auto state_is_valid = [&](const state_t &s) { /*...*/ };
// ݓ᫜ᒂݼ⟥ᔰ᭞ॕͩᝯⅱⰝᴶ
auto state_is_target = [&](const state_t &s) { /*...*/ };
// មᆄᒂݼ⟥ᔰ

---

172
せ9 』
ᎮᏕчٷ᥋㉑
auto state_extend = [&](const state_t &s) {
unordered_set<state_t> result;
for (/*...*/) {
const state_t new_state = /*...*/;
if (state_is_valid(new_state) &&
visited.find(new_state) != visited.end()) {
result.insert(new_state);
}
}
return result;
};
vector<vector<state_t> > result;
current.insert(start);
while (!current.empty()) {
++ level;
// ັ᳋ᒂݼ䌞ᒳ䪮Ꮥጡ㏾䊴䓶ᒂݼᰯⴜ䌞ᒳ䪮Ꮥ喌ञД͜ₑᄨ䄔䌞ᒳ⮳
// ำ⤵喌ఏͩᝀЛ㺰ឭ⮳᭞ᰯⴜ䌞ᒳ
if (!result.empty() && level+1 > result[0].size()) break;
// 1. ᐥ䔎ߏڔ visited, 䔈ᵦ᝼㘬ٰ䃧͓͙❥㞱◨ᠶीऻ̯͙ၿ㞱◨
// 2. ̯㗐㙀current ڗ䘗ߏڔ visited, ᭞䭡ₑᱛᅱݼ̯͙㞱◨មᆄ
// 㞱◨ᬥ喌ᠶीεᱛᅱऽ䲑ᅉ᱙ำ⤵⮳㞱◨喌䔈Ა䌞ᒳᓴ♥̼᭞ᰯⴜ⮳
for (const auto& state : current)
visited.insert(state);
for (const auto& state : current) {
if (state_is_target(state)) {
vector<string> path;
gen_path(father, path, start, state, result);
continue;
}
const auto new_states = state_extend(state);
for (const auto& new_state : new_states) {
next.insert(new_state);
father[new_state].push_back(state);
}
}
current.clear();
swap(current, next);
}
return result;
}
bfs_template.cpp

---

せ10 』
⌠Ꮥчٷ᥋㉑
10.1
Palindrome Partitioning
᣾䔟
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
For example, given s = "aab", Return
[
["aa","b"],
["a","a","b"]
]
ܵᲿ
౗⃾̯ₔ䘬ञДݓ᫜͜䬣㐂᳋᭞ॕͩष∄㐂᳋喌⩗఍⏞∄ȡ
̯͙䪮Ꮥͩ n ⮳ႆさ͡喌᰸n−1 ͙౟᫨ञДⴼ᫜喌⃾͙౟᫨ञ᫜ञ̼᫜喌ఏₓ฼ᱱᏕͩ O(2n−1)
⌠᥋1
//LeetCode, Palindrome Partitioning
// ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<string>> partition(string s) {
vector<vector<string>> result;
vector<string> path;
// ̯͙ partition ᫨ᵷ
dfs(s, path, result, 0, 1);
return result;
}
// prev 㶗⹩ݼ̯͙䯃Ხ, start 㶗⹩ᒂݼ䯃Ხ
void dfs(string &s, vector<string>& path,
vector<vector<string>> &result, size_t prev, size_t start) {
if (start == s.size()) { // ᰯऽ̯͙䯃Ხ
if (isPalindrome(s, prev, start - 1)) { // ᓴ䶪Ү⩗
path.push_back(s.substr(prev, start - prev));
173

---

174
せ10 』
⌠Ꮥчٷ᥋㉑
result.push_back(path);
path.pop_back();
}
return;
}
// ̼᫜ᐯ
dfs(s, path, result, prev, start + 1);
// ັ᳋[prev, start-1] ᭞఍᪶喌݈ञД᫜ᐯ喌ΎञД̼᫜ᐯ喈̹̯㵻ጡ㏾։ε喉
if (isPalindrome(s, prev, start - 1)) {
// ᫜ᐯ
path.push_back(s.substr(prev, start - prev));
dfs(s, path, result, start, start + 1);
path.pop_back();
}
}
bool isPalindrome(const string &s, int start, int end) {
while (start < end && s[start] == s[end]) {
++start;
--end;
}
return start >= end;
}
};
⌠᥋2
क̯⻼ۈ∄喌ᰣߏク∰ȡ䔈⻼ۈ∄Ύ౗Combination Sum, Combination Sum II ͜ܩ⣟䓶ȡ
//LeetCode, Palindrome Partitioning
// ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<string>> partition(string s) {
vector<vector<string>> result;
vector<string> path;
// ̯͙ partition ᫨ᵷ
DFS(s, path, result, 0);
return result;
}
// ᥋㉑ᓴ䶪Д s[start] ᐯ๣⮳partition ᫨ᵷ
void DFS(string &s, vector<string>& path,
vector<vector<string>> &result, int start) {
if (start == s.size()) {
result.push_back(path);
return;
}
for (int i = start; i < s.size(); i++) {
if (isPalindrome(s, start, i)) { // Ͻ i Ѽ㒝ⴼ̯ܯ
path.push_back(s.substr(start, i - start + 1));
DFS(s, path, result, i + 1);
// 㐖㐜ᒯ̺ⴼ
path.pop_back(); // ᧓䨯̹̹㵻
}
}

---

10.1
Palindrome Partitioning
175
}
bool isPalindrome(const string &s, int start, int end) {
while (start < end && s[start] == s[end]) {
++start;
--end;
}
return start >= end;
}
};
ߗ㻳
// LeetCode, Palindrome Partitioning
// ߗ㻳喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<vector<string> > partition(string s) {
const int n = s.size();
bool p[n][n]; // whether s[i,j] is palindrome
fill_n(&p[0][0], n * n, false);
for (int i = n - 1; i >= 0; --i)
for (int j = i; j < n; ++j)
p[i][j] = s[i] == s[j] && ((j - i < 2) || p[i + 1][j - 1]);
vector<vector<string> > sub_palins[n]; // sub palindromes of s[0,i]
for (int i = n - 1; i >= 0; --i) {
for (int j = i; j < n; ++j)
if (p[i][j]) {
const string palindrome = s.substr(i, j - i + 1);
if (j + 1 < n) {
for (auto v : sub_palins[j + 1]) {
v.insert(v.begin(), palindrome);
sub_palins[i].push_back(v);
}
} else {
sub_palins[i].push_back(vector<string> { palindrome });
}
}
}
return sub_palins[0];
}
};
Ⱗڢ题Ⱍ
• Palindrome Partitioning II喌㻰§13.3

---

176
せ10 』
⌠Ꮥчٷ᥋㉑
10.2
Unique Paths
᣾䔟
A robot is located at the top-left corner of a m × n grid (marked ’Start’ in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked ’Finish’ in the diagram below).
How many possible unique paths are there?
భ10-1
Above is a 3 × 7 grid. How many possible unique paths are there?
Note: m and n will be at most 100.
10.2.1
⌠᥋
⌠᥋喌ᄾ䯵षञД䓶喌๖䯵षщ䊴ᬥ
Вⴰ
// LeetCode, Unique Paths
// ⌠᥋喌ᄾ䯵षञД䓶喌๖䯵षщ䊴ᬥ
// ᬥ䬣฼ᱱᏕO(n^4)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int uniquePaths(int m, int n) {
if (m < 1 || n < 1) return 0; // ㏷ₑᲐХ
if (m == 1 && n == 1) return 1; // ᩥ᪊ᲐХ
return uniquePaths(m - 1, n) + uniquePaths(m, n - 1);
}
};
10.2.2
ึᔇᒄ∄
㐈ݼ䲑⮳⌠᥋喌ߏ͙㑂ႇ喌ᅠञД䓶๖䯵षεȡࢢึᔇᒄ∄ȡ

![Leetcode-CPP 第182页插图](../assets/images/Leetcode-CPP_p182_1_88048556.png)

---

10.2
Unique Paths
177
Вⴰ
// LeetCode, Unique Paths
// ⌠᥋+ 㑂ႇ喌ࢢึᔇᒄ∄
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
int uniquePaths(int m, int n) {
// f[x][y] 㶗⹩Ͻ (0,0) ݟ(x,y) ⮳䌞ᒳᲐ᪟
f = vector<vector<int> >(m, vector<int>(n, 0));
f[0][0] = 1;
return dfs(m - 1, n - 1);
}
private:
vector<vector<int> > f;
// 㑂ႇ
int dfs(int x, int y) {
if (x < 0 || y < 0) return 0; // ᪟ᢝ䲍∄喌㏷ₑᲐХ
if (x == 0 && y == 0) return f[0][0]; // ఍ݟ䊦◨喌ᩥ᪊ᲐХ
if (f[x][y] > 0) {
return f[x][y];
} else {
return f[x][y] = dfs(x - 1, y) +
dfs(x, y - 1);
}
}
};
10.2.3
ߗ㻳
ᬑ♥ञД⩗ึᔇᒄ∄㜙䶥ी̺解ۢ喌Ύ̯჉ञД⩗ߗ㻳㜙Ꮔी̹解ۢȡ
䃭⟥ᔰͩ f[i][j]喌㶗⹩Ͻ䊦◨(1, 1) ݟ䓭(i, j) ⮳䌞㏮Ა᪟喌݈⟥ᔰ䒛⼪᫨⼺ͩ喚
f[i][j]=f[i-1][j]+f[i][j-1]
Вⴰ
// LeetCode, Unique Paths
// ߗ㻳喌␉ߗ᪟㏳
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int uniquePaths(int m, int n) {
vector<int> f(n, 0);
f[0] = 1;
for (int i = 0; i < m; i++) {
for (int j = 1; j < n; j++) {
// ጕ䓨⮳f[j]喌㶗⹩ᰣ᫟ऽ⮳f[j]喌̽ڛᐾ͜⮳f[i][j] ᄨᏃ
// ढ䓨⮳f[j]喌㶗⹩㔰⮳f[j]喌̽ڛᐾ͜⮳f[i-1][j] ᄨᏃ
f[j] = f[j] + f[j - 1];
}

---

178
せ10 』
⌠Ꮥчٷ᥋㉑
}
return f[n - 1];
}
};
10.2.4
᪟႕ڛᐾ
̯͙ m 㵻喌n ݆⮳ⴘ䭤喌ᱩ஗ϩϽጕ̹䊟ݟढ̺ᕪڠ䰯㺰⮳ₔ᪟᭞m + n −2喌ڥ͜ी̺䊟⮳
ₔ᪟᭞m −1喌ఏₓ䬝题इ᜿ε౗m + n −2 ͙᧼ҋ͜喌䔸᠘m–1 ͙ᬥ䬣◨ी̺䊟喌䔸᠘᫨ᐾ᰸้
ᅀ⻼ȡࢢCm−1
m+n−2 ȡ
Вⴰ
// LeetCode, Unique Paths
// ᪟႕ڛᐾ
class Solution {
public:
typedef long long int64_t;
// ⅱ䭥·, n!/(start-1)!喌ࢢn*(n-1)...start喌㺰ⅱn >= 1
static int64_t factor(int n, int start = 1) {
int64_t
ret = 1;
for(int i = start; i <= n; ++i)
ret *= i;
return ret;
}
// ⅱ㏳ष᪟C_n^k
static int64_t combination(int n, int k) {
// ፧᪟чࡅ
if (k == 0) return 1;
if (k == 1) return n;
int64_t ret = factor(n, k+1);
ret /= factor(n - k);
return ret;
}
int uniquePaths(int m, int n) {
// max ञД䭡ₑ n ঻k ጝ䌌䓶๖喌Ͻ㔻䭡ₑ combination() ⏑ܩ
return combination(m+n-2, max(m-1, n-1));
}
};
Ⱗڢ题Ⱍ
• Unique Paths II喌㻰§10.3
• Minimum Path Sum, 㻰§13.8

---

10.3
Unique Paths II
179
10.3
Unique Paths II
᣾䔟
Follow up for ”Unique Paths”:
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3 × 3 grid as illustrated below.
[
[0,0,0],
[0,1,0],
[0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
10.3.1
ึᔇᒄ∄
౗̹̯题⮳ഩⵯ̹ᩨ̯̺ࢢञȡⰧ℃ߗ㻳喌クࢄᓆ้ȡ
Вⴰ
// LeetCode, Unique Paths II
// ⌠᥋+ 㑂ႇ喌ࢢึᔇᒄ∄
class Solution {
public:
int uniquePathsWithObstacles(const vector<vector<int> >& obstacleGrid) {
const int m = obstacleGrid.size();
const int n = obstacleGrid[0].size();
if (obstacleGrid[0][0] || obstacleGrid[m - 1][n - 1]) return 0;
f = vector<vector<int> >(m, vector<int>(n, 0));
f[0][0] = obstacleGrid[0][0] ? 0 : 1;
return dfs(obstacleGrid, m - 1, n - 1);
}
private:
vector<vector<int> > f;
// 㑂ႇ
// @return Ͻ (0, 0) ݟ(x, y) ⮳䌞ᒳᕪ᪟
int dfs(const vector<vector<int> >& obstacleGrid,
int x, int y) {
if (x < 0 || y < 0) return 0; // ᪟ᢝ䲍∄喌㏷ₑᲐХ
// (x,y) ᭞䯋ⶼ
if (obstacleGrid[x][y]) return 0;
if (x == 0 and y == 0) return f[0][0]; // ఍ݟ䊦◨喌ᩥ᪊ᲐХ

---

180
せ10 』
⌠Ꮥчٷ᥋㉑
if (f[x][y] > 0) {
return f[x][y];
} else {
return f[x][y] = dfs(obstacleGrid, x - 1, y) +
dfs(obstacleGrid, x, y - 1);
}
}
};
10.3.2
ߗ㻳
̹̯̽题ㆪѫ喌ѵ㺰➨ݚ∗ᘾせ̯݆⮳䯋ⶼȡ౗̹̯题͜喌せ̯݆ڗ䘗᭞1喌ѵ᭞౗䔈̯题̼͜
ऻ喌せ̯݆ັ᳋᳿̯㵻᰸䯋ⶼ➘喌䗒ͷऽ䲑⮳㵻ڗͩ 0ȡ
Вⴰ
// LeetCode, Unique Paths II
// ߗ㻳喌␉ߗ᪟㏳
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
const int m = obstacleGrid.size();
const int n = obstacleGrid[0].size();
if (obstacleGrid[0][0] || obstacleGrid[m-1][n-1]) return 0;
vector<int> f(n, 0);
f[0] = obstacleGrid[0][0] ? 0 : 1;
for (int i = 0; i < m; i++) {
f[0] = f[0] == 0 ? 0 : (obstacleGrid[i][0] ? 0 : 1);
for (int j = 1; j < n; j++)
f[j] = obstacleGrid[i][j] ? 0 : (f[j] + f[j - 1]);
}
return f[n - 1];
}
};
Ⱗڢ题Ⱍ
• Unique Paths喌㻰§10.2
• Minimum Path Sum, 㻰§13.8

---

10.4
N-Queens
181
10.4
N-Queens
᣾䔟
The n-queens puzzle is the problem of placing n queens on an n × n chessboard such that no two queens
attack each other.
భ10-2
Eight Queens
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.'
both indicate a queen and an empty space respectively.
For example, There exist two distinct solutions to the 4-queens puzzle:
[
[".Q..",
// Solution 1
"...Q",
"Q...",
"..Q."],
["..Q.",
// Solution 2
"Q...",
"...Q",
".Q.."]
]
ܵᲿ
㏾ڧ⮳⌠᥋题ȡ

![Leetcode-CPP 第187页插图](../assets/images/Leetcode-CPP_p187_1_694b81e2.png)

---

182
せ10 』
⌠Ꮥчٷ᥋㉑
䃭㒝̯͙᪟㏳vector<int> C(n, 0), C[i] 㶗⹩せi 㵻⮶ऽᝯ౗⮳݆㑅द喌ࢢ౗Ѽ㒝(i, C[i]) ̹
ᩭε̯͙⮶ऽ喌䔈ᵦ⩗̯͙̯㐣᪟㏳喌ᅠ㘬䃟ᒄ᪣᷺͙Ⰷȡ
Вⴰ1
// LeetCode, N-Queens
// ⌠᥋+ ޙ᳌
// ᬥ䬣฼ᱱᏕO(n!*n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<string> > solveNQueens(int n) {
vector<vector<string> > result;
vector<int> C(n, -1);
// C[i] 㶗⹩せi 㵻⮶ऽᝯ౗⮳݆㑅द
dfs(C, result, 0);
return result;
}
private:
void dfs(vector<int> &C, vector<vector<string> > &result, int row) {
const int N = C.size();
if (row == N) { // ㏷ₑᲐХ喌Ύ᭞ᩥ᪊ᲐХ喌ᘾঢⱯឭݟε̯͙ञ㵻解
vector<string> solution;
for (int i = 0; i < N; ++i) {
string s(N, '.');
for (int j = 0; j < N; ++j) {
if (j == C[i]) s[j] = 'Q';
}
solution.push_back(s);
}
result.push_back(solution);
return;
}
for (int j = 0; j < N; ++j) {
// មᆄ⟥ᔰ喌̯݆̯݆⮳䄄
const bool ok = isValid(C, row, j);
if (!ok) continue;
// ޙ᳌喌ັ᳋䲍∄喌㐖㐜ᅌ䄄̺̯݆
// ព㵻មᆄߗҋ
C[row] = j;
dfs(C, result, row + 1);
// ᧓䨯ߗҋ
// C[row] = -1;
}
}
/**
* 㘬ॕ౗(row, col) Ѽ㒝ᩭ̯͙⮶ऽ.
*
* @param C ᷺ᅯ
* @param row ᒂݼₒ౗ำ⤵⮳㵻喌ݼ䲑⮳㵻䘬ጡ㏾ᩭε⮶ऽε
* @param col ᒂݼ݆
* @return 㘬ॕᩭ̯͙⮶ऽ
*/
bool isValid(const vector<int> &C, int row, int col) {

---

10.4
N-Queens
183
for (int i = 0; i < row; ++i) {
// ౗ऻ̯݆
if (C[i] == col) return false;
// ౗ऻ̯ᄨ㼁㏮̹
if (abs(i - row) == abs(C[i] - col)) return false;
}
return true;
}
};
Вⴰ2
// LeetCode, N-Queens
// ⌠᥋+ ޙ᳌
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<string> > solveNQueens(int n) {
this->columns = vector<bool>(n, false);
this->main_diag = vector<bool>(2 * n - 1, false);
this->anti_diag = vector<bool>(2 * n - 1, false);
vector<vector<string> > result;
vector<int> C(n, -1);
// C[i] 㶗⹩せi 㵻⮶ऽᝯ౗⮳݆㑅द
dfs(C, result, 0);
return result;
}
private:
// 䔈̸͙इ䛾⩗νޙ᳌
vector<bool> columns;
// 㶗⹩ጡ㏾ᩭ㒝⮳⮶ऽ࢏ᢝεਙϊ݆
vector<bool> main_diag;
// ࢏ᢝεਙϊͪᄨ㼁㏮
vector<bool> anti_diag;
// ࢏ᢝεਙϊޞᄨ㼁㏮
void dfs(vector<int> &C, vector<vector<string> > &result, int row) {
const int N = C.size();
if (row == N) { // ㏷ₑᲐХ喌Ύ᭞ᩥ᪊ᲐХ喌ᘾঢⱯឭݟε̯͙ञ㵻解
vector<string> solution;
for (int i = 0; i < N; ++i) {
string s(N, '.');
for (int j = 0; j < N; ++j) {
if (j == C[i]) s[j] = 'Q';
}
solution.push_back(s);
}
result.push_back(solution);
return;
}
for (int j = 0; j < N; ++j) {
// មᆄ⟥ᔰ喌̯݆̯݆⮳䄄
const bool ok = !columns[j] && !main_diag[row - j + N - 1]
&&
!anti_diag[row + j];
if (!ok) continue;
// ޙ᳌喌ັ᳋䲍∄喌㐖㐜ᅌ䄄̺̯݆
// ព㵻មᆄߗҋ

---

184
せ10 』
⌠Ꮥчٷ᥋㉑
C[row] = j;
columns[j] = main_diag[row - j + N - 1] = anti_diag[row + j] = true;
dfs(C, result, row + 1);
// ᧓䨯ߗҋ
// C[row] = -1;
columns[j] = main_diag[row - j + N - 1] = anti_diag[row + j] = false;
}
}
};
Ⱗڢ题Ⱍ
• N-Queens II喌㻰§10.5
10.5
N-Queens II
᣾䔟
Follow up for N-Queens problem.
Now, instead outputting board configurations, return the total number of distinct solutions.
ܵᲿ
ङ䰯㺰䓂ܩ解⮳͙᪟喌̼䰯㺰䓂ܩᝯ᰸解喌Вⴰ㺰℃̹̯题クࡅᒷ้ȡ䃭̯͙ڗᅯ䃐᪟஗喌⃾ឭ
ݟ̯͙解ᅠ෍1ȡ
Вⴰ1
// LeetCode, N-Queens II
// ⌠᥋+ ޙ᳌
// ᬥ䬣฼ᱱᏕO(n!*n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int totalNQueens(int n) {
this->count = 0;
vector<int> C(n, 0);
// C[i] 㶗⹩せi 㵻⮶ऽᝯ౗⮳݆㑅द
dfs(C, 0);
return this->count;
}
private:
int count; // 解⮳͙᪟
void dfs(vector<int> &C, int row) {
const int N = C.size();
if (row == N) { // ㏷ₑᲐХ喌Ύ᭞ᩥ᪊ᲐХ喌ᘾঢⱯឭݟε̯͙ञ㵻解
++this->count;
return;

---

10.5
N-Queens II
185
}
for (int j = 0; j < N; ++j) {
// មᆄ⟥ᔰ喌̯݆̯݆⮳䄄
const bool ok = isValid(C, row, j);
if (!ok) continue;
// ޙ᳌喚ັ᳋ष∄喌㐖㐜䕁ᒁ
// ព㵻មᆄߗҋ
C[row] = j;
dfs(C, row + 1);
// ᧓䨯ߗҋ
// C[row] = -1;
}
}
/**
* 㘬ॕ౗(row, col) Ѽ㒝ᩭ̯͙⮶ऽ.
*
* @param C ᷺ᅯ
* @param row ᒂݼₒ౗ำ⤵⮳㵻喌ݼ䲑⮳㵻䘬ጡ㏾ᩭε⮶ऽε
* @param col ᒂݼ݆
* @return 㘬ॕᩭ̯͙⮶ऽ
*/
bool isValid(const vector<int> &C, int row, int col) {
for (int i = 0; i < row; ++i) {
// ౗ऻ̯݆
if (C[i] == col) return false;
// ౗ऻ̯ᄨ㼁㏮̹
if (abs(i - row) == abs(C[i] - col)) return false;
}
return true;
}
};
Вⴰ2
// LeetCode, N-Queens II
// ⌠᥋+ ޙ᳌
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int totalNQueens(int n) {
this->count = 0;
this->columns = vector<bool>(n, false);
this->main_diag = vector<bool>(2 * n - 1, false);
this->anti_diag = vector<bool>(2 * n - 1, false);
vector<int> C(n, 0);
// C[i] 㶗⹩せi 㵻⮶ऽᝯ౗⮳݆㑅द
dfs(C, 0);
return this->count;
}
private:
int count; // 解⮳͙᪟
// 䔈̸͙इ䛾⩗νޙ᳌
vector<bool> columns;
// 㶗⹩ጡ㏾ᩭ㒝⮳⮶ऽ࢏ᢝεਙϊ݆
vector<bool> main_diag;
// ࢏ᢝεਙϊͪᄨ㼁㏮

---

186
せ10 』
⌠Ꮥчٷ᥋㉑
vector<bool> anti_diag;
// ࢏ᢝεਙϊޞᄨ㼁㏮
void dfs(vector<int> &C, int row) {
const int N = C.size();
if (row == N) { // ㏷ₑᲐХ喌Ύ᭞ᩥ᪊ᲐХ喌ᘾঢⱯឭݟε̯͙ञ㵻解
++this->count;
return;
}
for (int j = 0; j < N; ++j) {
// មᆄ⟥ᔰ喌̯݆̯݆⮳䄄
const bool ok = !columns[j] &&
!main_diag[row - j + N] &&
!anti_diag[row + j];
if (!ok) continue;
// ޙ᳌喚ັ᳋ष∄喌㐖㐜䕁ᒁ
// ព㵻មᆄߗҋ
C[row] = j;
columns[j] = main_diag[row - j + N] =
anti_diag[row + j] = true;
dfs(C, row + 1);
// ᧓䨯ߗҋ
// C[row] = -1;
columns[j] = main_diag[row - j + N] =
anti_diag[row + j] = false;
}
}
};
Ⱗڢ题Ⱍ
• N-Queens喌㻰§10.4
10.6
Restore IP Addresses
᣾䔟
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example: Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
ܵᲿ
ᓴ䶪㺰䊟ݟᏄ䘗᝼㘬ݓ᫜解᭞ॕष∄喌⌠᥋ȡ
Вⴰ
// LeetCode, Restore IP Addresses
// ᬥ䬣฼ᱱᏕO(n^4)喌⾩䬣฼ᱱᏕO(n)
class Solution {

---

10.6
Restore IP Addresses
187
public:
vector<string> restoreIpAddresses(const string& s) {
vector<string> result;
vector<string> ip; // ႇᩭ͜䬣㐂᳋
dfs(s, ip, result, 0);
return result;
}
/**
* @brief 解Ჿႆさ͡
* @param[in] s ႆさ͡喌䓂ڔ᪟ᢝ
* @param[out] ip ႇᩭ͜䬣㐂᳋
* @param[out] result ႇᩭᝯ᰸ञ㘬⮳IP ౟౯
* @param[in] start ᒂݼₒ౗ำ⤵⮳index
* @return ᬏ
*/
void dfs(string s, vector<string>& ip, vector<string> &result,
size_t start) {
if (ip.size() == 4 && start == s.size()) {
// ឭݟ̯͙ष∄解
result.push_back(ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + ip[3]);
return;
}
if (s.size() - start > (4 - ip.size()) * 3)
return;
// ޙ᳌
if (s.size() - start < (4 - ip.size()))
return;
// ޙ᳌
int num = 0;
for (size_t i = start; i < start + 3; i++) {
num = num * 10 + (s[i] - '0');
if (num < 0 || num > 255) continue;
// ޙ᳌
ip.push_back(s.substr(start, i - start + 1));
dfs(s, ip, result, i + 1);
ip.pop_back();
if (num == 0) break;
// ٰ̼䃧ݼ㐯0喌ѵٰ䃧ࢄ͙ 0
}
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

188
せ10 』
⌠Ꮥчٷ᥋㉑
10.7
Combination Sum
᣾䔟
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
• All numbers (including target) will be positive integers.
• Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (ie, a1 ≤a2 ≤... ≤ak).
• The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, A solution set is:
[7]
[2, 2, 3]
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Combination Sum
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > combinationSum(vector<int> &nums, int target) {
sort(nums.begin(), nums.end());
vector<vector<int> > result; // ᰯ㏷㐂᳋
vector<int> path; // ͜䬣㐂᳋
dfs(nums, path, result, target, 0);
return result;
}
private:
void dfs(vector<int>& nums, vector<int>& path, vector<vector<int> > &result,
int gap, int start) {
if (gap == 0) {
// ឭݟ̯͙ष∄解
result.push_back(path);
return;
}
for (size_t i = start; i < nums.size(); i++) { // មᆄ⟥ᔰ
if (gap < nums[i]) return; // ޙ᳌
path.push_back(nums[i]); // ព㵻មᆄߗҋ
dfs(nums, path, result, gap - nums[i], i);
path.pop_back();
// ᧓䨯ߗҋ
}

---

10.8
Combination Sum II
189
}
};
Ⱗڢ题Ⱍ
• Combination Sum II 喌㻰§10.8
10.8
Combination Sum II
᣾䔟
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in
C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
• All numbers (including target) will be positive integers.
• Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (ie, a1 > a2 > ... > ak).
• The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Combination Sum II
// ᬥ䬣฼ᱱᏕO(n!)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > combinationSum2(vector<int> &nums, int target) {
sort(nums.begin(), nums.end()); // 䌎せ50 㵻䙼ष喌
// ⶝Ԍ⃾͙ٲ㉏ᰯ้ङ⩗̯⁐
vector<vector<int> > result;
vector<int> path;
dfs(nums, path, result, target, 0);
return result;
}
private:
// Ү⩗nums[start, nums.size()) ͺ䬣⮳ٲ㉏喌㘬ឭݟ⮳ᝯ᰸ञ㵻解

---

190
せ10 』
⌠Ꮥчٷ᥋㉑
static void dfs(const vector<int> &nums, vector<int> &path,
vector<vector<int> > &result, int gap, int start) {
if (gap == 0) {
//
ឭݟ̯͙ष∄解
result.push_back(path);
return;
}
int previous = -1;
for (size_t i = start; i < nums.size(); i++) {
// ັ᳋̹̯䒝ᓙ⣞ጡ㏾Ү⩗ε nums[i]喌݈ᱛ⁐ᓙ⣞ᅠ̼㘬ڼ䔸nums[i]喌
// ⶝Ԍ nums[i] ᰯ้ङ⩗̯⁐
if (previous == nums[i]) continue;
if (gap < nums[i]) return;
// ޙ᳌
previous = nums[i];
path.push_back(nums[i]);
dfs(nums, path, result, gap - nums[i], i + 1);
path.pop_back();
// ᖑ฼⣞඲
}
}
};
Ⱗڢ题Ⱍ
• Combination Sum 喌㻰§10.7
10.9
Generate Parentheses
᣾䔟
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
ܵᲿ
ᄾ᠛द͡᭞̯͙䕁ᒁ㐂Ჳ喌䌎ࢄ䨭㶗Ƞλࣸᵀへ䕁ᒁ㐂Ჳ̯ᵦ喌仅ٷᘢݟ⩗䕁ᒁȡ
̯ₔₔᲳ䕏ႆさ͡ȡᒂጕ᠛दܩ⣟⁐᪟< n ᬥ喌ᅠञДᩭ㒝᫟⮳ጕ᠛दȡᒂढ᠛दܩ⣟⁐᪟ᄾ
νጕ᠛दܩ⣟⁐᪟ᬥ喌ᅠञДᩭ㒝᫟⮳ढ᠛दȡ
Вⴰ1
// LeetCode, Generate Parentheses
// ᬥ䬣฼ᱱᏕO(TODO)喌⾩䬣฼ᱱᏕO(n)
class Solution {

---

10.9
Generate Parentheses
191
public:
vector<string> generateParenthesis(int n) {
vector<string> result;
string path;
if (n > 0) generate(n, path, result, 0, 0);
return result;
}
// l 㶗⹩( ܩ⣟⮳⁐᪟, r 㶗⹩) ܩ⣟⮳⁐᪟
void generate(int n, string& path, vector<string> &result, int l, int r) {
if (l == n) {
string s(path);
result.push_back(s.append(n - r, ')'));
return;
}
path.push_back('(');
generate(n, path, result, l + 1, r);
path.pop_back();
if (l > r) {
path.push_back(')');
generate(n, path, result, l, r + 1);
path.pop_back();
}
}
};
Вⴰ2
क̯⻼䕁ᒁۈ∄喌ᰣߏク∰ȡ
// LeetCode, Generate Parentheses
// @author 䔍೽(http://weibo.com/lianchengzju)
class Solution {
public:
vector<string> generateParenthesis (int n) {
if (n == 0) return vector<string>(1, "");
if (n == 1) return vector<string> (1, "()");
vector<string> result;
for (int i = 0; i < n; ++i)
for (auto inner : generateParenthesis (i))
for (auto outer : generateParenthesis (n - 1 - i))
result.push_back ("(" + inner + ")" + outer);
return result;
}
};
Ⱗڢ题Ⱍ
• Valid Parentheses, 㻰§4.1.1

---

192
せ10 』
⌠Ꮥчٷ᥋㉑
• Longest Valid Parentheses, 㻰§4.1.2
10.10
Sudoku Solver
᣾䔟
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
భ10-3
A sudoku puzzle...
భ10-4
...and its solution numbers marked in red
ܵᲿ
ᬏȡ

![Leetcode-CPP 第198页插图](../assets/images/Leetcode-CPP_p198_1_6edaa7d2.png)

![Leetcode-CPP 第198页插图](../assets/images/Leetcode-CPP_p198_2_80cb219a.png)

---

10.11
Word Search
193
Вⴰ
// LeetCode, Sudoku Solver
// ᬥ䬣฼ᱱᏕO(9^4)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool solveSudoku(vector<vector<char> > &board) {
for (int i = 0; i < 9; ++i)
for (int j = 0; j < 9; ++j) {
if (board[i][j] == '.') {
for (int k = 0; k < 9; ++k) {
board[i][j] = '1' + k;
if (isValid(board, i, j) && solveSudoku(board))
return true;
board[i][j] = '.';
}
return false;
}
}
return true;
}
private:
// ᷯᴔ(x, y) ᭞ॕष∄
bool isValid(const vector<vector<char> > &board, int x, int y) {
int i, j;
for (i = 0; i < 9; i++) // ᷯᴔy ݆
if (i != x && board[i][y] == board[x][y])
return false;
for (j = 0; j < 9; j++) // ᷯᴔx 㵻
if (j != y && board[x][j] == board[x][y])
return false;
for (i = 3 * (x / 3); i < 3 * (x / 3 + 1); i++)
for (j = 3 * (y / 3); j < 3 * (y / 3 + 1); j++)
if ((i != x || j != y) && board[i][j] == board[x][y])
return false;
return true;
}
};
Ⱗڢ题Ⱍ
• Valid Sudoku, 㻰§2.1.14
10.11
Word Search
᣾䔟
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighbouring. The same letter cell may not be used more than once.

---

194
せ10 』
⌠Ꮥчٷ᥋㉑
For example, Given board =
[
["ABCE"],
["SFCS"],
["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
ܵᲿ
ᬏȡ
Вⴰ
// LeetCode, Word Search
// ⌠᥋喌䕁ᒁ
// ᬥ䬣฼ᱱᏕO(n^2*m^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
bool exist(const vector<vector<char> > &board, const string& word) {
const int m = board.size();
const int n = board[0].size();
vector<vector<bool> > visited(m, vector<bool>(n, false));
for (int i = 0; i < m; ++i)
for (int j = 0; j < n; ++j)
if (dfs(board, word, 0, i, j, visited))
return true;
return false;
}
private:
static bool dfs(const vector<vector<char> > &board, const string &word,
int index, int x, int y, vector<vector<bool> > &visited) {
if (index == word.size())
return true; // ᩥ᪊ᲐХ
if (x < 0 || y < 0 || x >= board.size() || y >= board[0].size())
return false;
// 䊹⩻喌㏷ₑᲐХ
if (visited[x][y]) return false; // ጡ㏾䃮䬝䓶喌ޙ᳌
if (board[x][y] != word[index]) return false; // ̼Ⱗへ喌ޙ᳌
visited[x][y] = true;
bool ret = dfs(board, word, index + 1, x - 1, y, visited) || // ̹
dfs(board, word, index + 1, x + 1, y, visited)
|| // ̺
dfs(board, word, index + 1, x, y - 1, visited)
|| // ጕ
dfs(board, word, index + 1, x, y + 1, visited);
// ढ
visited[x][y] = false;

---

10.12
ᄾ㐂
195
return ret;
}
};
Ⱗڢ题Ⱍ
• ᬏ
10.12
ᄾ㐂
10.12.1
䔱⩗౩ᮞ
䓂ڔ᪟ᢝ喚ັ᳋᭞䕁ᒁ᪟ᢝ㐂Ჳ喌ັࢄ䨭㶗喌λࣸᵀ喌䯵ष喌݈⮭ܵͺ⮭ञД⩗⌠᥋喛ັ᳋᭞䲍
䕁ᒁ᪟ᢝ㐂Ჳ喌ັ̯㐣᪟㏳喌λ㐣᪟㏳喌ႆさ͡喌భ喌݈ằ⢶ᄾ̯ϊȡ
⟥ᔰ䒛ᢑభ喚ᵀᝅ㔴భȡ
ⅱ解Ⱍᴶ喚ᓴ䶪㺰䊟ݟᰯ⌠喈Һັᄨνᵀ喌ᓴ䶪㺰䊟ݟथၿ㞱◨喉᝼㘬ᓆݟ̯͙解喌䔈⻼ᗴۤ䔱
ष⩗⌠᥋ȡ
10.12.2
ᕌ㔲⮳ₔ俓
1. ᭞ⅱ䌞ᒳᲐ᪟喌䔇᭞䌞ᒳᱛ䏚喈ᝅߗҋᎾ݆喉喟⌠᥋ᰯ፧㻰⮳̸͙䬝题喌ⅱञ㵻解⮳ᕪ᪟喌ⅱ
̯͙ञ㵻解喌ⅱᝯ᰸ञ㵻解ȡ
(a) ັ᳋᭞䌞ᒳᲐ᪟喌݈̼䰯㺰ႇח䌞ᒳȡ
(b) ັ᳋᭞ⅱ䌞ᒳᱛ䏚喌݈㺰⩗̯͙᪟㏳path[] ႇח䌞ᒳȡ䌎წ᥋̼ऻ喌წ᥋㮬♥ᰯ㏷ⅱ
⮳Ύ᭞̯Ა䌞ᒳ喌ѵ᭞䰯㺰ႇחមᆄ䓶⼺͜⮳ᝯ᰸䌞ᒳ喌౗⇐ឭݟゃᵷͺݼᝯ᰸䌞ᒳ䘬
̼㘬ᩭᐲ喛㔻⌠᥋喌౗᥋㉑䓶⼺͜໺㏷ङ᰸̯Ა䌞ᒳ喌ఏₓ⩗̯͙᪟㏳ᅠ䋢๎εȡ
2. ङ㺰ⅱ̯͙解喌䔇᭞㺰ⅱᝯ᰸解喟ັ᳋ङ㺰ⅱ̯͙解喌䗒ឭݟ̯͙ᅠञД䔃఍喛ັ᳋㺰ⅱᝯ᰸
解喌ឭݟε̯͙ऽ喌䔇㺰㐖㐜មᆄ喌Ⱓݟ䕼ࢵႻȡᎮ᥋̯㝛ङ㺰ⅱ̯͙解喌ఏ㔻̼䰯㺰㔲㮀䔈
͙䬝题喈Ꭾ᥋ᒂ♥ΎञДⅱᝯ᰸解喌䔈ᬥ䰯㺰មᆄݟᝯ᰸थၿ㞱◨喌Ⱗᒂν౗ڴႇ͜ႇח᪣͙
⟥ᔰ䒛ᢑభ喌䲍፧࢏ڴႇ喌ఏₓᎮ᥋̼䔱ष解䔈ㆪ䬝题喉ȡ
3. ັ҄㶗⹩⟥ᔰ喟ࢢ̯͙⟥ᔰ䰯㺰ႇחਙϊϊᓴ㺰⮳᪟ᢝ喌᝼㘬๎Ⴛ᪣᣿ӊັ҄មᆄݟ̺̯ₔ
⟥ᔰ⮳ᝯ᰸Ԑᖞȡ䌎Ꭾ᥋̼ऻ喌⌠᥋⮳ᘞ⩗ۈ∄喌̼᭞ឹ᪟ᢝ䃟ᒄ౗⟥ᔰstruct 䛻喌㔻᭞〉
ߏܬ᪟ࣱ᪟喈᰸ᬥͩε㞱ⰰ䕁ᒁവᴷ喌⩗ڗᅯइ䛾喉喌struct 䛻⮳ႆ⃤̽ܬ᪟ࣱ᪟̯̯ᄨᏃȡ
4. ັ҄មᆄ⟥ᔰ喟䔈̯ₔ䌎̹̯ₔⰧڢȡ⟥ᔰ䛻䃟ᒄ⮳᪟ᢝ̼ऻ喌មᆄ᫨∄ᅠ̼ऻȡᄨν఩჉̼
इ⮳᪟ᢝ㐂Ჳ喈̯㝛题ⰝⰣᣔ㐈ܩ喌ҋͩ䓂ڔ᪟ᢝ喉喌ັλࣸᵀ喌భへ喌មᆄ᫨∄ᒷクࢄ喌Ⱓ
ᣔᒯ̺̯ᅱ䊟喌ᄨν䮿ᐾభ喌㺰ٷ౗せ1 ₔ䛻ᘢ⌴ẉ⟥ᔰᝯፕ⮳᪟ᢝ喌ᘢ⌴ẉε䔈◨喌䗒ັ҄
មᆄᅠᒷクࢄεȡ

---

196
せ10 』
⌠Ꮥчٷ᥋㉑
5. ㏷ₑᲐХ᭞ϯͷ喟㏷ₑᲐХ᭞ᠶݟε̼㘬មᆄ⮳ᱚ〞㞱◨ȡᄨνᵀ喌᭞थၿ㞱◨喌ᄨνభᝅ䮿
ᐾభ喌᭞ܩᏕͩ 0 ⮳㞱◨ȡ
6. ᩥ᪊ᲐХ᭞ϯͷ喟ᩥ᪊ᲐХ᭞ᠶឭݟε̯͙ष∄解⮳ᬥݪȡັ᳋᭞ₒी⌠᥋喈❥⟥ᔰำ⤵Ⴛε
᝼䔊㵻䕁ᒁ喌ࢢ❥⟥ᔰ̼ӌ䊅ၿ⟥ᔰ喌䕁ᒁ䄜औ̯჉᭞౗ᰯऽ喌ᅭ䕁ᒁ喉喌݈᭞ᠶ᭞ॕ䓭ݟⰝ
ᴶ⟥ᔰ喛ັ᳋᭞䔵ी⌠᥋喈ำ⤵❥⟥ᔰᬥ䰯㺰ٷⴔ䖂ၿ⟥ᔰ⮳㐂᳋喌ₓᬥ䕁ᒁ䄜औ̼౗ᰯऽ喉喌
݈᭞ᠶ᭞ॕݟ䓭݌໺⟥ᔰȡ
⩠νᒷ้ᬥՈ㏷ₑᲐХ঻ᩥ᪊ᲐХ᭞᭞षλ̯ͩ⮳喌ఏₓᒷ้ϩ̼ࡩܵ䔈͓⻼ᲐХȡЃ㏵ࡩܵ
䔈͓⻼ᲐХ喌䔇᭞ᒷ᰸ᓴ㺰⮳ȡ
ͩεݓ᫜᭞ॕݟεᩥ᪊ᲐХ喌㺰౗ܬ᪟ᣔऒ䛻⩗ࣱ̯͙᪟䃟ᒄᒂݼ⮳Ѽ㒝喈ᝅ䌌⻪Ⱍᴶ䔇᰸้
䔋喉ȡັ᳋᭞ⅱ̯͙解喌Ⱓᣔ䔃఍䔈͙解喛ັ᳋᭞ⅱᝯ᰸解喌㺰౗䔈䛻ᩥ䯵解喌ࢢឹせ̯ₔ͜
㶗⹩䌞ᒳ⮳᪟㏳path[] ฼ݥݟ解䯵ष䛻ȡ
7. ڢνݓ䛼
(a) ᭞ॕ䰯㺰ݓ䛼喟ັ᳋⟥ᔰ䒛ᢑభ᭞̯Ḥᵀ喌݈̼䰯㺰ݓ䛼喌ఏͩ౗䕼ࢵ䓶⼺̼͜ञ㘬䛼
฼喛ັ᳋⟥ᔰ䒛ᢑభ᭞̯͙ DAG喌݈䰯㺰ݓ䛼ȡ䔈̯◨䌎BFS ̼̯ᵦ喌BFS ⮳⟥ᔰ䒛ᢑ
భᕪ᭞DAG喌ᓴ䶪㺰ݓ䛼ȡ
(b) ᔽᵦݓ䛼喟䌎Ꭾ᥋Ⱗऻ喌㻰せ§9.4 㞱ȡऻᬥ喌DAG 䄣ᬽႇ౗䛼एၿ䬝题喌ₓᬥञД⩗㑂
ႇߏ䕎喌㻰せ8 ₔȡ
8. ັ҄ߏ䕎喟
(a) ޙ᳌ȡ⌠᥋̯჉㺰ຬຬ㔲㮀ᔽͷޙ᳌喌᜿ᱛᄾᩥ⯹๖喌ߏ܏㵻Вⴰ喌ᅠ㘬๖๖ߏ䕎ȡ䔈
䛻⇐᰸䕉⩗᫨∄喌ङ㘬ڦ҂䬝题ڦ҂ܵᲿ喌㺰ٴܵ㻱ᄎ喌ٴܵݘ⩗ळ⻼ԐᖞᲔޙ᳌喌౗
͜䬣㞱◨᣿ݼ䔃఍ȡ
(b) 㑂ႇȡ
i. ݼ᣿ᲐХ喚⟥ᔰ䒛ᢑభ᭞̯͙ DAGȡDAG=> ႇ౗䛼एၿ䬝题=> ၿ䬝题⮳解щ㷚
䛼฼ݘ⩗喌⩗㑂ႇ㜙♥щ᰸ߏ䕎᩷᳋ȡັ᳋ӌ䊅ڢ㈪᭞ᵀ⟥⮳喈Һັᵀ喌ࢄ䨭㶗へ喉喌
⇐ᓴ㺰ߏ㑂ႇ喌ఏͩၿ䬝题ङщ̯ᅱᅱᒯ̺喌⩗̯⁐ᅠڼΎ̼щ⩗ݟ喌ߏε㑂ႇΎ
⇐ϯͷߏ䕎᩷᳋ȡ
ii. ڦ҂Ⴭ⣟喚ञД⩗᪟㏳ᝅHashMapȡ㐣Ꮥクࢄ⮳喌⩗᪟㏳喛㐣Ꮥ฼ᱱ⮳喌⩗HashMap喌
C++ ᰸map喌C++ 11 Дऽ᰸unordered_map喌℃map ᔚȡ
ᠮݟ̯͙题Ⱍ喌ᒂᙎ㻸Ⴒ䔱ष⩗⌠᥋解ۢᬥ喌౗ᓲ䛻䲑ឹ̹䲑8 ͙䬝题吇吇఍ゃ̯䕼喌Вⴰഩᱛ
̹ᅠ㘬ۈܩᲔεȡᄨνᵀ喌̼䰯㺰఍ゃせ5 ঻せ8 ͙䬝题ȡັ᳋䄪㔴ᄨ̹䲑⮳㏾侻ᕪ㐂ⰺ̼ᛱᝅᙎ㻸
Ć̼Ⴭ⩗ć喌ᒷₒ፧喌ఏͩ䔈ϊ㏾侻ᕪ㐂᭞ᝀ։εᒷ้题Ⱍऽᕪ㐂ܩᲔ⮳喌Ͻᕌ㐣⮳ऀᆄ䓶⼺ⰺ喌Ć㏾
侻ᕪ㐂ć㺰ᮉνᙎᕖ䃓䃵喌ᝯД䔈ᬥՈᐩ䃝䄪㔴ٷ։։ݼ䲑⮳题Ⱍ喌⼞㉞̯჉⮳ᙎᕖ䃓䃵ऽ喌ڼ఍䓶
๣Ეⰺ䔈̯㞱⮳ᕪ㐂喌̯჉щ᰸ڠ卒ȡ

---

10.12
ᄾ㐂
197
10.12.3
ВⴰὐᲮ
dfs_template.cpp
/**
* dfs ὐᲮ.
* @param[in] input 䓂ڔ᪟ᢝᠶ䦷
* @param[out] path ᒂݼ䌞ᒳ喌Ύ᭞͜䬣㐂᳋
* @param[out] result ႇᩭᰯ㏷㐂᳋
* @param[inout] cur or gap ᴶ䃟ᒂݼѼ㒝ᝅ䌌⻪Ⱍᴶ⮳䌌⻪
* @return 䌞ᒳ䪮Ꮥ喌ັ᳋᭞ⅱ䌞ᒳᱛ䏚喌݈̼䰯㺰䔃఍䪮Ꮥ
*/
void dfs(type &input, type &path, type &result, int cur or gap) {
if (᪟ᢝ䲍∄) return 0;
// ㏷ₑᲐХ
if (cur == input.size()) { // ᩥ᪊ᲐХ
// if (gap == 0) {
ᄵpath ᩭڔ result
}
if (ञДޙ᳌) return;
for(...) { // ព㵻ᝯ᰸ञ㘬⮳មᆄߗҋ
ព㵻ߗҋ喌ԝᩨpath
dfs(input, step + 1 or gap--, result);
ᖑ฼path
}
}
dfs_template.cpp
10.12.4
⌠᥋̽఍⏞∄⮳ࡩݚ
⌠᥋(Depth-first search, DFS) ⮳჉͸㻰http://en.wikipedia.org/wiki/Depth_ﬁrst_search喌఍⏞∄(backtrack-
ing) ⮳჉͸㻰http://en.wikipedia.org/wiki/Backtracking
఍⏞∄= ⌠᥋+ ޙ᳌ȡ̯㝛๖ქ⩗⌠᥋ᬥ喌ᝅ้ᝅᅀщޙ᳌喌ఏₓ⌠᥋̽఍⏞∄⇐᰸ϯͷ̼ऻ喌
ञД౗ႲЛͺ䬣⩪̹̯͙へदȡᱛΕऻᬥҮ⩗⌠᥋঻఍⏞∄͓͙ᱞ䄜喌ѵ䄪㔴ञД䃓ͩλ㔴へЦȡ
⌠᥋̯㝛⩗䕁ᒁ(recursion) ᲔჍ⣟喌䔈ᵦ℃䒲ク∰ȡ
⌠᥋㘬๎౗Ո䔸ゃᵷ⩎᜿ݟ̯ࡹᬥ喌ᅠ䔊㵻ݓ᫜喌៊ᐲ̼␐䋢㺰ⅱ⮳ゃᵷ喌ᝯД⌠᥋℃ᯣߊ᥋
㉑∄㺰ᔚȡ
10.12.5
⌠᥋̽䕁ᒁ⮳ࡩݚ
⌠᥋㏾፧⩗䕁ᒁ(recursion) ᲔჍ⣟喌λ㔴፧፧ऻᬥܩ⣟喌ᄫ㜣ᒷ้ϩ䄞ДͩЅԘ᭞̯͙͋㺮ȡ
⌠᥋喌᭞䕪䓀ᘾ͸̹⮳テ∄喌䕁ᒁ喌᭞̯⻼➘⤵ᘾ͸̹⮳Ⴭ⣟喌Ⴒ঻䔜В (iteration) ᭞ᄨᏃ⮳ȡ⌠
᥋喌ञД⩗䕁ᒁᲔჍ⣟喌ΎञД⩗ᴷᲔჍ⣟喛㔻䕁ᒁ喌̯㝛ᕪ᭞⩗ᲔჍ⣟⌠᥋ȡञД䄣喌䕁ᒁ̯჉᭞
⌠᥋喌⌠᥋̼̯჉⩗䕁ᒁȡ
䕁ᒁ᰸͓⻼ߏ䕎ゅ⪔喌̯⻼᭞ޙ᳌(prunning)喌ᄨ͜䬣㐂᳋䔊㵻ݓ᫜喌᣿ݼ䔃఍喛̯⻼᭞㑂ႇ喌
㑂ႇ͜䬣㐂᳋喌䭡ₑ䛼฼䃐テ喌⩗⾩䬣ᢑᬥ䬣ȡ

---

198
せ10 』
⌠Ꮥчٷ᥋㉑
ڥჍ喌䕁ᒁ+ 㑂ႇ喌ᅠ᭞memorizationȡᝯ䅂memorization喈㔪䄀ͩึᔇᒄ∄喌㻰せ§??㞱喉喌ᅠ
᭞”top-down with cache”喈㜙䶥ी̺ + 㑂ႇ喉喌Ⴒ᭞Donald Michie ౗1968 Ꭳ݊䕏⮳ᱞ䄜喌㶗⹩̯⻼ч
ࡅឯᱞ喌౗top-down ᒑᐾ⮳⼺Ꮎ͜喌Ү⩗㑂ႇᲔ䖮ټ䛼฼䃐テ喌Ͻ㔻䓭ݟߏ䕎⮳Ⱍ⮳ȡ
memorization ̼̯჉⩗䕁ᒁ喌ᅠ׾⌠᥋̼̯჉⩗䕁ᒁ̯ᵦ喌ञД౗䔜В (iterative) ͜Ү⩗memo-
rization ȡ䕁ᒁΎ̼̯჉⩗memorization喌ञД⩗memorization Ეߏ䕎喌ѵ̼᭞ᓴ䶪⮳ȡङ᰸ᒂ䕁ᒁ
Ү⩗ε㑂ႇ喌Ⴒ᝼᭞memorization ȡ
ᬑ♥䕁ᒁ̯჉᭞⌠᥋喌ͩϯͷᒷ้Εㅼ䘬ऻᬥҮ⩗䔈͓͙ᱞ䄜঑喟౗䕁ᒁঢ䖂ᰣ⊂⮳౟᫨喌̯
㝛⩗䕁ᒁ䔈͙ᱞ䄜喌౗⌠᥋ᰣ⊂⮳౩ᮞ̺喌⩗⌠᥋䔈͙ᱞ䄜喌䄪㔴ᓲ䛻㺰ᐳ⌴ẉЅԘ๖䘗ܵᬥՈ᭞
̯఍κȡ౗ࢄ䨭㶗Ƞλࣸᵀへ䕁ᒁ᪟ᢝ㐂Ჳ̹喌䕁ᒁ⮳ঢ䖂ᰣ⊂喌䔈ᬥ⩗䕁ᒁ䔈͙ᱞ䄜喛౗భȠ䮿ᐾ
భへ᪟ᢝ㐂Ჳ̹喌⌠᥋⮳ঢ䖂ᰣ⊂喌䔈ᬥ⩗⌠᥋䔈͙ᱞ䄜ȡ

---

せ11 』
ܵ⇪∄
11.1
Pow(x,n)
᣾䔟
Implement pow(x, n).
ܵᲿ
λܵ∄喌xn = xn/2 × xn/2 × xn%2
Вⴰ
//LeetCode, Pow(x, n)
// λܵ∄喌$x^n = x^{n/2} * x^{n/2} * x^{n\%2}$
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
double myPow(double x, int n) {
if (n < 0) return 1.0 / power(x, -n);
else return power(x, n);
}
private:
double power(double x, int n) {
if (n == 0) return 1;
double v = power(x, n / 2);
if (n % 2 == 0) return v * v;
else return v * v * x;
}
};
Ⱗڢ题Ⱍ
• Sqrt(x)喌㻰§11.2
199

---

200
せ11 』
ܵ⇪∄
11.2
Sqrt(x)
᣾䔟
Implement int sqrt(int x).
Compute and return the square root of x.
ܵᲿ
λܵᴔឭ
Вⴰ
// LeetCode, Sqrt(x)
// λܵᴔឭ
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int mySqrt(int x) {
int left = 1, right = x / 2;
int last_mid;
// 䃟ᒄᰯ䔀̯⁐ mid
if (x < 2) return x;
while(left <= right) {
const int mid = left + (right - left) / 2;
if(x / mid > mid) { // ̼㺰⩗x > mid * mid喌щ⏑ܩ
left = mid + 1;
last_mid = mid;
} else if(x / mid < mid) {
right = mid - 1;
} else {
return mid;
}
}
return last_mid;
}
};
Ⱗڢ题Ⱍ
• Pow(x)喌㻰§11.1

---

せ12 』
䉙ᓲ∄
12.1
Jump Game
᣾䔟
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
ܵᲿ
⩠ν⃾ᅱᰯ้ञД䌢A[i] ₔ喌ΎञД䌢0 ᝅ1 ₔ喌ఏₓັ᳋㘬ݟ䓭ᰯ倇ᅱ喌݈䄣ᬽ⃾̯ᅱ䘬ञ
Дݟ䓭ȡ᰸ε䔈͙ᲐХ喌䄣ᬽञД⩗䉙ᓲ∄ȡ
ᕌ䌞̯喚ₒी喌Ͻ 0 ܩऀ喌̯ᅱ̯ᅱ㒀̹䌢喌ⰺᰯऽ㘬̼㘬䊴䓶ᰯ倇ᅱ喌㘬䊴䓶喌䄣ᬽ㘬ݟ䓭喌
ॕ݈̼㘬ݟ䓭ȡ
ᕌ䌞λ喚䔵ी喌Ͻᰯ倇ᅱ̺ẫᷞ喌̯ᅱ̯ᅱ̺䭼喌ⰺᰯऽ㘬̼㘬̺䭼ݟせ0 ᅱȡ
ᕌ䌞̸喚ັ᳋̼᪑⩗䉙ᓲ喌ञД⩗ߗ㻳喌䃭⟥ᔰͩ f[i]喌㶗⹩Ͻせ0 ᅱܩऀ喌䊟ݟA[i] ᬥޘ
҈⮳ᰯ๖ₔ᪟喌݈⟥ᔰ䒛⼪᫨⼺ͩ喚
f[i] = max(f[i −1], A[i −1]) −1, i > 0
Вⴰ1
// LeetCode, Jump Game
// ᕌ䌞1喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool canJump(const vector<int>& nums) {
int reach = 1; // ᰯढ㘬䌢ݟਙ䛻
for (int i = 0; i < reach && reach < nums.size(); ++i)
reach = max(reach,
i + 1 + nums[i]);
201

---

202
せ12 』
䉙ᓲ∄
return reach >= nums.size();
}
};
Вⴰ2
// LeetCode, Jump Game
// ᕌ䌞2喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool canJump (const vector<int>& nums) {
if (nums.empty()) return true;
// 䔵ी̺ẫᷞ喌ᰯጕ㘬̺䭼ݟせ܏ᅱ
int left_most = nums.size() - 1;
for (int i = nums.size() - 2; i >= 0; --i)
if (i + nums[i] >= left_most)
left_most = i;
return left_most == 0;
}
};
Вⴰ3
// LeetCode, Jump Game
// ᕌ䌞̸喌ߗ㻳喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
bool canJump(const vector<int>& nums) {
vector<int> f(nums.size(), 0);
f[0] = 0;
for (int i = 1; i < nums.size(); i++) {
f[i] = max(f[i - 1], nums[i - 1]) - 1;
if (f[i] < 0) return false;;
}
return f[nums.size() - 1] >= 0;
}
};
Ⱗڢ题Ⱍ
• Jump Game II 喌㻰§12.2
12.2
Jump Game II
᣾䔟
Given an array of non-negative integers, you are initially positioned at the first index of the array.

---

12.2
Jump Game II
203
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example: Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps
to the last index.)
ܵᲿ
䉙ᓲ∄ȡ
Вⴰ1
// LeetCode, Jump Game II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int jump(const vector<int>& nums) {
int step = 0; // ᰯᄾₔ᪟
int left = 0;
int right = 0;
// [left, right] ᭞ᒂݼ㘬㺵Ⰵ⮳ࡩ䬣
if (nums.size() == 1) return 0;
while (left <= right) { // ᅌ䄄Ͻ⃾̯ᅱ䌢ᰯ䔋
++step;
const int old_right = right;
for (int i = left; i <= old_right; ++i) {
int new_right = i + nums[i];
if (new_right >= nums.size() - 1) return step;
if (new_right > right) right = new_right;
}
left = old_right + 1;
}
return 0;
}
};
Вⴰ2
// LeetCode, Jump Game II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int jump(const vector<int>& nums) {
int result = 0;
// the maximum distance that has been reached
int last = 0;
// the maximum distance that can be reached by using "ret+1" steps
int cur = 0;

---

204
せ12 』
䉙ᓲ∄
for (int i = 0; i < nums.size(); ++i) {
if (i > last) {
last = cur;
++result;
}
cur = max(cur, i + nums[i]);
}
return result;
}
};
Ⱗڢ题Ⱍ
• Jump Game 喌㻰§12.1
12.3
Best Time to Buy and Sell Stock
᣾䔟
Say you have an array for which the i-th element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the
stock), design an algorithm to find the maximum profit.
ܵᲿ
䉙ᓲ∄喌ܵݚឭݟЦᵫᰯѽ঻ᰯ倇⮳̯๘喌ѽ䔊倇ܩ喌∗ᘾᰯѽ⮳̯๘㺰౗ᰯ倇⮳̯๘ͺݼȡ
ឹ࣎໺ЦᵫᎾ݆इ᜿ጝܵᎾ݆喌ᱛ题ΎञД։᭞ᰯ๖m ၿ⃤঻喌m = 1ȡ
Вⴰ
// LeetCode, Best Time to Buy and Sell Stock
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int maxProfit(vector<int> &prices) {
if (prices.size() < 2) return 0;
int profit = 0;
// ጝЦ喌Ύᅠ᭞ݘ⋕
int cur_min = prices[0]; // ᒂݼᰯᄾ
for (int i = 1; i < prices.size(); i++) {
profit = max(profit, prices[i] - cur_min);
cur_min = min(cur_min, prices[i]);
}
return profit;
}
};

---

12.4
Best Time to Buy and Sell Stock II
205
Ⱗڢ题Ⱍ
• Best Time to Buy and Sell Stock II喌㻰§12.4
• Best Time to Buy and Sell Stock III喌㻰§13.5
12.4
Best Time to Buy and Sell Stock II
᣾䔟
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie,
buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions
at the same time (ie, you must sell the stock before you buy again).
ܵᲿ
䉙ᓲ∄喌ѽ䔊倇ܩ喌ឹᝯ᰸ₒ⮳ЦᵫጝЦⰧߏ䊦Ეȡ
ឹ࣎໺ЦᵫᎾ݆इ᜿ጝܵᎾ݆喌ᱛ题ΎञД։᭞ᰯ๖m ၿ⃤঻喌m = ᪟㏳䪮Ꮥȡ
Вⴰ
// LeetCode, Best Time to Buy and Sell Stock II
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int maxProfit(vector<int> &prices) {
int sum = 0;
for (int i = 1; i < prices.size(); i++) {
int diff = prices[i] - prices[i - 1];
if (diff > 0) sum += diff;
}
return sum;
}
};
Ⱗڢ题Ⱍ
• Best Time to Buy and Sell Stock喌㻰§12.3
• Best Time to Buy and Sell Stock III喌㻰§13.5

---

206
せ12 』
䉙ᓲ∄
12.5
Longest Substring Without Repeating Characters
᣾䔟
Given a string, find the length of the longest substring without repeating characters. For example, the
longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the
longest substring is "b", with the length of 1.
ܵᲿ
ն䃭ၿ͡䛻ग़᰸䛼฼ႆさ喌݈❥̯͡჉ग़᰸䛼฼ႆさ喌ࢄ͙ၿ䬝题ᅠञДۢ჉❥䬝题喌ఏₓञ
Д⩗䉙ᓲ∄ȡ䌎ߗ㻳̼ऻ喌ߗ㻳䛻喌ࢄ͙ၿ䬝题ङ㘬ᒠৼ❥䬝题喌̼䋢Дۢ჉❥䬝题ȡ
Ͻጕᒯढរ᣾喌ᒂ䕶ݟ䛼฼ႆ⃼ᬥ喌Д̹̯͙䛼฼ႆ⃼⮳index+1喌ҋͩ᫟⮳᥋㉑䊦໺Ѽ㒝喌Ⱓ
ݟᰯऽ̯͙ႆ⃼喌฼ᱱᏕ᭞O(n)ȡັభ12-1ᝯ⹩ȡ
భ12-1
̼ग़䛼฼ႆさ⮳ᰯ䪮ၿ͡
Вⴰ
// LeetCode, Longest Substring Without Repeating Characters
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
// 㔲㮀䲍ႆ⃼⮳ᗴۤ
class Solution {
public:
int lengthOfLongestSubstring(string s) {
const int ASCII_MAX = 255;
int last[ASCII_MAX]; // 䃟ᒄႆさ̹⁐ܩ⣟䓶⮳Ѽ㒝
int start = 0; // 䃟ᒄᒂݼၿ͡⮳䊦໺Ѽ㒝
fill(last, last + ASCII_MAX, -1); // 0 Ύ᭞᰸᩷Ѽ㒝喌ఏₓ݌໺ࡅͩ-1
int max_len = 0;
for (int i = 0; i < s.size(); i++) {
if (last[s[i]] >= start) {
max_len = max(i - start, max_len);
start = last[s[i]] + 1;
}
last[s[i]] = i;
}

![Leetcode-CPP 第212页插图](../assets/images/Leetcode-CPP_p212_1_2caf2d24.png)

---

12.6
Container With Most Water
207
return max((int)s.size() - start, max_len);
// ݚᔇεᰯऽ̯⁐喌Һັ"abcd"
}
};
Ⱗڢ题Ⱍ
• ᬏ
12.6
Container With Most Water
᣾䔟
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n verti-
cal lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
ܵᲿ
⃾͙შ஗⮳䲑⼞喌अۢνᰯⴜ⮳᱗Ხȡ
Вⴰ
// LeetCode, Container With Most Water
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int maxArea(vector<int> &height) {
int start = 0;
int end = height.size() - 1;
int result = INT_MIN;
while (start < end) {
int area = min(height[end], height[start]) * (end - start);
result = max(result, area);
if (height[start] <= height[end]) {
start++;
} else {
end--;
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• Trapping Rain Water, 㻰§2.1.15

---

208
せ12 』
䉙ᓲ∄
• Largest Rectangle in Histogram, 㻰§4.1.3

---

せ13 』
ߗᔰ㻳݁
13.1
Triangle
᣾䔟
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent
numbers on the row below.
For example, given the following triangle
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of
rows in the triangle.
ܵᲿ
䃭⟥ᔰͩ f(i, j)喌㶗⹩ϽϽѼ㒝(i, j) ܩऀ喌䌞ᒳ⮳ᰯᄾ঻喌݈⟥ᔰ䒛⼪᫨⼺ͩ
f(i, j) = min {f(i + 1, j), f(i + 1, j + 1)} + (i, j)
Вⴰ
// LeetCode, Triangle
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int minimumTotal (vector<vector<int>>& triangle) {
for (int i = triangle.size() - 2; i >= 0; --i)
for (int j = 0; j < i + 1; ++j)
triangle[i][j] += min(triangle[i + 1][j],
triangle[i + 1][j + 1]);
209

---

210
せ13 』
ߗᔰ㻳݁
return triangle [0][0];
}
};
Ⱗڢ题Ⱍ
• ᬏ
13.2
Maximum Subarray
᣾䔟
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has
the largest sum = 6.
ܵᲿ
ᰯ๖䔍㐜ၿᎾ݆঻喌䲍፧㏾ڧ⮳题ȡ
ᒂᝀЛϽ๣ݟᅭ䕼ࢵ䔈͙᪟㏳⮳ᬥՈ喌ᄨν᪟㏳䛻⮳̯͙᪣᪟喌Ⴒ᰸܏⻼䔸᠘঑喟Ⴒङ᰸͓⻼
䔸᠘喚1Ƞߏڔͺݼ⮳SubArray喛2. 㜙ጠक䊦̯͙ SubArrayȡ䗒ϯͷᬥՈщܩ⣟䔈͓⻼ᗴۤ঑喟
ັ᳋ͺݼSubArray ⮳ᕪ҂঻๖ν 0 ⮳䄌喌ᝀЛ䃓ͩڥᄨऽ㐜㐂᳋᭞᰸䉐⡝⮳ȡ䔈⻼ᗴ̺ۤᝀЛ
䔸᠘ߏڔͺݼ⮳SubArray
ັ᳋ͺݼSubArray ⮳ᕪ҂঻ͩ 0 ᝅ㔴ᄾν 0 ⮳䄌喌ᝀЛ䃓ͩڥᄨऽ㐜㐂᳋᭞⇐᰸䉐⡝喌⩉㜢᭞
᰸ტ⮳喈ᄾν 0 ᬥ喉ȡ䔈⻼ᗴ̺ۤᝀЛ䔸᠘Д䔈͙᪟ႆᐯ໺喌क䊦̯͙ SubArrayȡ
䃭⟥ᔰͩ f[j]喌㶗⹩Д S[j] 㐂ᅭ⮳ᰯ๖䔍㐜ၿᎾ݆঻喌݈⟥ᔰ䒛⼪᫨⼺ັ̺喚
f[j]
=
max {f[j −1] + S[j], S[j]} , ڥ͜1 ≤j ≤n
target
=
max {f[j]} , ڥ͜1 ≤j ≤n
解䛹ັ̺喚
• ᗴ̯ۤ喌S[j] ̼⠛⿺喌̽ݼ䲑⮳᳿ϊ᪟㏳᜿̯͙䔍㐜ၿᎾ݆喌݈ᰯ๖䔍㐜ၿᎾ݆঻ͩ f[j −1] +
S[j]ȡ
• ᗴۤλ喌S[j] ⠛⿺݁ܵ᜿̯ͩ⃤喌ࢢ䔍㐜ၿᎾ݆ϴ࠴ग़̯͙᪟S[j]喌݈ᰯ๖䔍㐜ၿᎾ݆঻ͩ S[j]ȡ
ڥЅᕌ䌞喚
• ᕌ䌞2喚Ⱓᣔ౗i ݟj ͺ䬣ᯣߊ᳉ͭ喌฼ᱱᏕ᭞O(n3)
• ᕌ䌞3喚ำ⤵ऽ᳉ͭ喌䔍㐜ၿᎾ݆⮳঻へν͓͙ݼ㐯঻ͺጝ喌฼ᱱᏕO(n2)ȡ
• ᕌ䌞4喚ܵ⇪∄喌ឹᎾ݆͓ܵͩ⃤喌ܵݚⅱᰯ๖䔍㐜ၿᎾ݆঻喌♥ऽᒁᎥ喌฼ᱱᏕO(n log n)
• ᕌ䌞5喚ឹᕌ䌞2O(n2) ⮳Вⴰ⼼ҋำ⤵喌ᓆݟO(n) ⮳テ∄
• ᕌ䌞6喚ᒂ᜿M=1 ⮳ᰯ๖M ၿ⃤঻

---

13.2
Maximum Subarray
211
ߗ㻳
// LeetCode, Maximum Subarray
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int maxSubArray(vector<int>& nums) {
int result = INT_MIN, f = 0;
for (int i = 0; i < nums.size(); ++i) {
f = max(f + nums[i], nums[i]);
result = max(result, f);
}
return result;
}
};
ᕌ䌞5
// LeetCode, Maximum Subarray
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int maxSubArray(vector<int>& A) {
return mcss(A.begin(), A.end());
}
private:
// ᕌ䌞5喌ⅱᰯ๖䔍㐜ၿᎾ݆঻
template <typename Iter>
static int mcss(Iter begin, Iter end) {
int result, cur_min;
const int n = distance(begin, end);
int *sum = new int[n + 1];
// ݼn 䶨঻
sum[0] = 0;
result = INT_MIN;
cur_min = sum[0];
for (int i = 1; i <= n; i++) {
sum[i] = sum[i - 1] + *(begin
+ i - 1);
}
for (int i = 1; i <= n; i++) {
result = max(result, sum[i] - cur_min);
cur_min = min(cur_min, sum[i]);
}
delete[] sum;
return result;
}
};
Ⱗڢ题Ⱍ
• Binary Tree Maximum Path Sum喌㻰§5.4.5

---

212
せ13 』
ߗᔰ㻳݁
13.3
Palindrome Partitioning II
᣾䔟
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
ܵᲿ
჉͸⟥ᔰf(i,j) 㶗⹩ࡩ䬣[i,j] ͺ䬣ᰯᄾ⮳cut ᪟喌݈⟥ᔰ䒛⼪᫨⼺ͩ
f(i, j) = min {f(i, k) + f(k + 1, j)} , i ≤k ≤j, 0 ≤i ≤j < n
䔈᭞̯͙λ㐣ܬ᪟喌Ⴭ䭴ۈВⴰ℃䒲只☕ȡ
ᝯД㺰䒛ᢑ᜿̯㐣DPȡັ᳋⃾⁐喌Ͻ i ᒯढរ᣾喌⃾ឭݟ̯͙఍᪶ᅠテ̯⁐ DP ⮳䄌喌ᅠञД
䒛ᢑͩ f(i)= ࡩ䬣[i, n-1] ͺ䬣ᰯᄾ⮳cut ᪟喌n ͩႆさ͡䪮Ꮥ喌݈⟥ᔰ䒛⼪᫨⼺ͩ
f(i) = min {f(j + 1) + 1} , i ≤j < n
̯͙䬝题ܩ⣟ε喌ᅠ᭞ັ҄ݓ᫜[i,j] ᭞ॕ᭞఍᪶喟⃾⁐䘬Ͻ i ݟj ℃䒲̯䕼喟๙⊙䉨ε喌䔈
䛻Ύ᭞̯͙ DP 䬝题ȡ
჉͸⟥ᔰP[i][j] = true if [i,j] ͩ఍᪶喌䗒ͷ
P[i][j] = str[i] == str[j] && P[i+1][j-1]
Вⴰ
// LeetCode, Palindrome Partitioning II
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
int minCut(const string& s) {
const int n = s.size();
int f[n+1];
bool p[n][n];
fill_n(&p[0][0], n * n, false);
//the worst case is cutting by each char
for (int i = 0; i <= n; i++)
f[i] = n - 1 - i; // ᰯऽ̯͙ f[n]=-1
for (int i = n - 1; i >= 0; i--) {
for (int j = i; j < n; j++) {
if (s[i] == s[j] && (j - i < 2 || p[i + 1][j - 1])) {
p[i][j] = true;
f[i] = min(f[i], f[j + 1] + 1);
}
}

---

13.4
Maximal Rectangle
213
}
return f[0];
}
};
Ⱗڢ题Ⱍ
• Palindrome Partitioning喌㻰§10.1
13.4
Maximal Rectangle
᣾䔟
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return
its area.
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Maximal Rectangle
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int maximalRectangle(vector<vector<char> > &matrix) {
if (matrix.empty())
return 0;
const int m = matrix.size();
const int n = matrix[0].size();
vector<int> H(n, 0);
vector<int> L(n, 0);
vector<int> R(n, n);
int ret = 0;
for (int i = 0; i < m; ++i) {
int left = 0, right = n;
// calculate L(i, j) from left to right
for (int j = 0; j < n; ++j) {
if (matrix[i][j] == '1') {
++H[j];
L[j] = max(L[j], left);
} else {
left = j+1;
H[j] = 0; L[j] = 0; R[j] = n;
}
}

---

214
せ13 』
ߗᔰ㻳݁
// calculate R(i, j) from right to left
for (int j = n-1; j >= 0; --j) {
if (matrix[i][j] == '1') {
R[j] = min(R[j], right);
ret = max(ret, H[j]*(R[j]-L[j]));
} else {
right = j;
}
}
}
return ret;
}
};
Ⱗڢ题Ⱍ
• ᬏ
13.5
Best Time to Buy and Sell Stock III
᣾䔟
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before
you buy again).
ܵᲿ
䃭⟥ᔰf(i)喌㶗⹩ࡩ䬣[0, i](0 ≤i ≤n−1) ⮳ᰯ๖ݘ⋕喌⟥ᔰg(i)喌㶗⹩ࡩ䬣[i, n−1](0 ≤i ≤n−1)
⮳ᰯ๖ݘ⋕喌݈ᰯ㏷ゃᵷͩ max {f(i) + g(i)} , 0 ≤i ≤n −1ȡ
ٰ䃧౗̯๘ڴΟ䔊ࣷࢅܩ喌Ⱗᒂν̼ϓᭂ喌ఏͩ题Ⱍ⮳㻳჉᭞ᰯ้͓⁐喌㔻̼᭞̯჉㺰͓⁐ȡ
ᄵ࣎᪟㏳इ᜿ጝܵ᪟㏳喌ᱛ题ΎञДⰺ։᭞ᰯ๖m ၿ⃤঻喌m
=
2喌ࣱ㔲Вⴰ喚
https://gist.github.com/soulmachine/5906637
Вⴰ
// LeetCode, Best Time to Buy and Sell Stock III
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int maxProfit(vector<int>& prices) {
if (prices.size() < 2) return 0;
const int n = prices.size();
vector<int> f(n, 0);

---

13.6
Interleaving String
215
vector<int> g(n, 0);
for (int i = 1, valley = prices[0]; i < n; ++i) {
valley = min(valley, prices[i]);
f[i] = max(f[i - 1], prices[i] - valley);
}
for (int i = n - 2, peak = prices[n - 1]; i >= 0; --i) {
peak = max(peak, prices[i]);
g[i] = max(g[i], peak - prices[i]);
}
int max_profit = 0;
for (int i = 0; i < n; ++i)
max_profit = max(max_profit, f[i] + g[i]);
return max_profit;
}
};
Ⱗڢ题Ⱍ
• Best Time to Buy and Sell Stock喌㻰§12.3
• Best Time to Buy and Sell Stock II喌㻰§12.4
13.6
Interleaving String
᣾䔟
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
For example, Given: s1 = "aabcc", s2 = "dbbca",
When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
ܵᲿ
䃭⟥ᔰf[i][j]喌㶗⹩s1[0,i] ঻s2[0,j]喌ࡨ䙼s3[0, i+j]ȡັ᳋s1 ⮳ᰯऽ̯͙ႆさへν
s3 ⮳ᰯऽ̯͙ႆさ喌݈f[i][j]=f[i-1][j]喛ັ᳋s2 ⮳ᰯऽ̯͙ႆさへν s3 ⮳ᰯऽ̯͙ႆさ喌݈
f[i][j]=f[i][j-1]ȡఏₓ⟥ᔰ䒛⼪᫨⼺ັ̺喚
f[i][j] = (s1[i - 1] == s3 [i + j - 1] && f[i - 1][j])
|| (s2[j - 1] == s3 [i + j - 1] && f[i][j - 1]);
䕁ᒁ
// LeetCode, Interleaving String
// 䕁ᒁ喌щ䊴ᬥ喌ϴ⩗Ე፝ߘ⤵解

---

216
せ13 』
ߗᔰ㻳݁
class Solution {
public:
bool isInterleave(const string& s1, const string& s2, const string& s3) {
if (s3.length() != s1.length() + s2.length())
return false;
return isInterleave(begin(s1), end(s1), begin(s2), end(s2),
begin(s3), end(s3));
}
template<typename InIt>
bool isInterleave(InIt first1, InIt last1, InIt first2, InIt last2,
InIt first3, InIt last3) {
if (first3 == last3)
return first1 == last1 && first2 == last2;
return (*first1 == *first3
&& isInterleave(next(first1), last1, first2, last2,
next(first3), last3))
|| (*first2 == *first3
&& isInterleave(first1, last1, next(first2), last2,
next(first3), last3));
}
};
ߗ㻳
// LeetCode, Interleaving String
// λ㐣ߗ㻳喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
bool isInterleave(const string& s1, const string& s2, const string& s3) {
if (s3.length() != s1.length() + s2.length())
return false;
vector<vector<bool>> f(s1.length() + 1,
vector<bool>(s2.length() + 1, true));
for (size_t i = 1; i <= s1.length(); ++i)
f[i][0] = f[i - 1][0] && s1[i - 1] == s3[i - 1];
for (size_t i = 1; i <= s2.length(); ++i)
f[0][i] = f[0][i - 1] && s2[i - 1] == s3[i - 1];
for (size_t i = 1; i <= s1.length(); ++i)
for (size_t j = 1; j <= s2.length(); ++j)
f[i][j] = (s1[i - 1] == s3[i + j - 1] && f[i - 1][j])
|| (s2[j - 1] == s3[i + j - 1] && f[i][j - 1]);
return f[s1.length()][s2.length()];
}
};

---

13.7
Scramble String
217
ߗ㻳+ ␉ߗ᪟㏳
// LeetCode, Interleaving String
// λ㐣ߗ㻳+ ␉ߗ᪟㏳喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
bool isInterleave(const string& s1, const string& s2, const string& s3) {
if (s1.length() + s2.length() != s3.length())
return false;
if (s1.length() < s2.length())
return isInterleave(s2, s1, s3);
vector<bool> f(s2.length() + 1, true);
for (size_t i = 1; i <= s2.length(); ++i)
f[i] = s2[i - 1] == s3[i - 1] && f[i - 1];
for (size_t i = 1; i <= s1.length(); ++i) {
f[0] = s1[i - 1] == s3[i - 1] && f[0];
for (size_t j = 1; j <= s2.length(); ++j)
f[j] = (s1[i - 1] == s3[i + j - 1] && f[j])
|| (s2[j - 1] == s3[i + j - 1] && f[j - 1]);
}
return f[s2.length()];
}
};
Ⱗڢ题Ⱍ
• ᬏ
13.7
Scramble String
᣾䔟
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings
recursively.
Below is one possible representation of s1 = "great":
great
/
\
gr
eat
/ \
/
\
g
r
e
at
/ \
a
t

---

218
せ13 』
ߗᔰ㻳݁
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node "gr" and swap its two children, it produces a scrambled string
"rgeat".
rgeat
/
\
rg
eat
/ \
/
\
r
g
e
at
/ \
a
t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string
"rgtae".
rgtae
/
\
rg
tae
/ \
/
\
r
g
ta
e
/ \
t
a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
ܵᲿ
仅ٷᘢݟ⮳᭞䕁ᒁ喈ࢢ⌠᥋喉喌ᄨ͓͙ string 䔊㵻ܵޡ喌♥ऽ℃䒲ఊᄨႆさ͡ȡВⴰ㮬♥クࢄ喌
ѵ᭞฼ᱱᏕ℃䒲倇ȡ᰸͓⻼ߏ䕎ゅ⪔喌̯⻼᭞ޙ᳌喌᣿ݼ䔃఍喛̯⻼᭞ߏ㑂ႇ喌㑂ႇ͜䬣㐂᳋喌ࢢ
memorization喈㔪䄀ͩ䃟ᓵࡅ᥋㉑喉ȡ
ޙ᳌ञДσ㟠ښ䬗喌㺰ٴܵ㻱ᄎ喌ٴܵݘ⩗Ԑᖞ喌ឭݟ㘬䃘㞱◨᣿ݼ䔃఍⮳ᲐХȡҺັ喌ݓ᫜͓
͙ႆさ͡᭞ॕρͩ scamble喌㜢ᅀ㺰ⅱ⃾͙ႆさ౗͓͙ႆさ͜͡ܩ⣟⮳⁐᪟㺰Ⱗへ喌ັ᳋̼Ⱗへ݈䔃
఍falseȡ
ߏ㑂ႇ喌ञД⩗᪟㏳ᝅHashMapȡᱛ题㐣᪟䒲倇喌⩗HashMap喌map ঻unordered_map ౶ञȡ
ᬑ♥ञД⩗䃟ᓵࡅ᥋㉑喌䔈题Ύ̯჉ञД⩗ߗ㻳ȡ䃭⟥ᔰͩ f[n][i][j]喌㶗⹩䪮Ꮥͩ n喌䊦◨
ͩ s1[i] ঻䊦◨ͩ s2[j] ͓͙ႆさ͡᭞ॕρͩ scramble喌݈⟥ᔰ䒛⼪᫨⼺ͩ
f[n][i][j]} =
(f[k][i][j] && f[n-k][i+k][j+k])
|| (f[k][i][j+n-k] && f[n-k][i+k][j])
䕁ᒁ
// LeetCode, Scramble String
// 䕁ᒁ喌щ䊴ᬥ喌ϴ⩗Ე፝ߘ⤵解
// ᬥ䬣฼ᱱᏕO(n^6)喌⾩䬣฼ᱱᏕO(1)
class Solution {

---

13.7
Scramble String
219
public:
bool isScramble(const string& s1, const string& s2) {
return isScramble(s1.begin(), s1.end(), s2.begin());
}
private:
typedef string::iterator Iterator;
bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
auto length = distance(first1, last1);
auto last2 = next(first2, length);
if (length == 1) return *first1 == *first2;
for (int i = 1; i < length; ++i)
if ((isScramble(first1, first1 + i, first2)
&& isScramble(first1 + i, last1, first2 + i))
|| (isScramble(first1, first1 + i, last2 - i)
&& isScramble(first1 + i, last1, first2)))
return true;
return false;
}
};
ߗ㻳
// LeetCode, Scramble String
// ߗ㻳喌ᬥ䬣฼ᱱᏕO(n^3)喌⾩䬣฼ᱱᏕO(n^3)
class Solution {
public:
bool isScramble(const string& s1, const string& s2) {
const int N = s1.size();
if (N != s2.size()) return false;
// f[n][i][j]喌㶗⹩䪮Ꮥͩ n喌䊦◨ͩ s1[i] ঻
// 䊦◨ͩ s2[j] ͓͙ႆさ͡᭞ॕρͩ scramble
bool f[N + 1][N][N];
fill_n(&f[0][0][0], (N + 1) * N * N, false);
for (int i = 0; i < N; i++)
for (int j = 0; j < N; j++)
f[1][i][j] = s1[i] == s2[j];
for (int n = 1; n <= N; ++n) {
for (int i = 0; i + n <= N; ++i) {
for (int j = 0; j + n <= N; ++j) {
for (int k = 1; k < n; ++k) {
if ((f[k][i][j] && f[n - k][i + k][j + k]) ||
(f[k][i][j + n - k] && f[n - k][i + k][j])) {
f[n][i][j] = true;
break;
}
}
}

---

220
せ13 』
ߗᔰ㻳݁
}
}
return f[N][0][0];
}
};
䕁ᒁ+ ޙ᳌
// LeetCode, Scramble String
// 䕁ᒁ+ ޙ᳌
// ᬥ䬣฼ᱱᏕO(n^6)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
bool isScramble(const string& s1, const string& s2) {
return isScramble(s1.begin(), s1.end(), s2.begin());
}
private:
typedef string::const_iterator Iterator;
bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
auto length = distance(first1, last1);
auto last2 = next(first2, length);
if (length == 1) return *first1 == *first2;
// ޙ᳌喌᣿ݼ䔃఍
int A[26]; // ⃾͙ႆさ⮳䃐᪟஗
fill(A, A + 26, 0);
for(int i = 0; i < length; i++) A[*(first1+i)-'a']++;
for(int i = 0; i < length; i++) A[*(first2+i)-'a']--;
for(int i = 0; i < 26; i++) if (A[i] != 0) return false;
for (int i = 1; i < length; ++i)
if ((isScramble(first1, first1 + i, first2)
&& isScramble(first1 + i, last1, first2 + i))
|| (isScramble(first1, first1 + i, last2 - i)
&& isScramble(first1 + i, last1, first2)))
return true;
return false;
}
};
ึᔇᒄ∄
// LeetCode, Scramble String
// 䕁ᒁ+map ։ cache
// ᬥ䬣฼ᱱᏕO(n^3)喌⾩䬣฼ᱱᏕO(n^3), TLE
class Solution {
public:
bool isScramble(const string& s1, const string& s2) {
cache.clear();
return isScramble(s1.begin(), s1.end(), s2.begin());
}

---

13.7
Scramble String
221
private:
typedef string::const_iterator Iterator;
map<tuple<Iterator, Iterator, Iterator>, bool> cache;
bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
auto length = distance(first1, last1);
auto last2 = next(first2, length);
if (length == 1) return *first1 == *first2;
for (int i = 1; i < length; ++i)
if ((getOrUpdate(first1, first1 + i, first2)
&& getOrUpdate(first1 + i, last1, first2 + i))
|| (getOrUpdate(first1, first1 + i, last2 - i)
&& getOrUpdate(first1 + i, last1, first2)))
return true;
return false;
}
bool getOrUpdate(Iterator first1, Iterator last1, Iterator first2) {
auto key = make_tuple(first1, last1, first2);
auto pos = cache.find(key);
return (pos != cache.end()) ?
pos->second : (cache[key] = isScramble(first1, last1, first2));
}
};
ึᔇᒄ∄
typedef string::const_iterator Iterator;
typedef tuple<Iterator, Iterator, Iterator> Key;
// ჉ݥ̯͙৷ጻܬ᪟
namespace std {
template<> struct hash<Key> {
size_t operator()(const Key & x) const {
Iterator first1, last1, first2;
tie(first1, last1, first2) = x;
int result = *first1;
result = result * 31 + *last1;
result = result * 31 + *first2;
result = result * 31 + *(next(first2, distance(first1, last1)-1));
return result;
}
};
}
// LeetCode, Scramble String
// 䕁ᒁ+unordered_map ։ cache喌℃map ᔚ
// ᬥ䬣฼ᱱᏕO(n^3)喌⾩䬣฼ᱱᏕO(n^3)
class Solution {

---

222
せ13 』
ߗᔰ㻳݁
public:
unordered_map<Key, bool> cache;
bool isScramble(const string& s1, const string& s2) {
cache.clear();
return isScramble(s1.begin(), s1.end(), s2.begin());
}
bool isScramble(Iterator first1, Iterator last1, Iterator first2) {
auto length = distance(first1, last1);
auto last2 = next(first2, length);
if (length == 1)
return *first1 == *first2;
for (int i = 1; i < length; ++i)
if ((getOrUpdate(first1, first1 + i, first2)
&& getOrUpdate(first1 + i, last1, first2 + i))
|| (getOrUpdate(first1, first1 + i, last2 - i)
&& getOrUpdate(first1 + i, last1, first2)))
return true;
return false;
}
bool getOrUpdate(Iterator first1, Iterator last1, Iterator first2) {
auto key = make_tuple(first1, last1, first2);
auto pos = cache.find(key);
return (pos != cache.end()) ?
pos->second : (cache[key] = isScramble(first1, last1, first2));
}
};
Ⱗڢ题Ⱍ
• ᬏ
13.8
Minimum Path Sum
᣾䔟
Given a m × n grid filled with non-negative numbers, find a path from top left to bottom right which
minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time
ܵᲿ
䌎Unique Paths (㻰§10.2) ᒷㆪѫȡ

---

13.8
Minimum Path Sum
223
䃭⟥ᔰͩ f[i][j]喌㶗⹩Ͻ䊦◨(0, 0) ݟ䓭(i, j) ⮳ᰯᄾ䌞ᒳ঻喌݈⟥ᔰ䒛⼪᫨⼺ͩ喚
f[i][j]=min(f[i-1][j], f[i][j-1])+grid[i][j]
ึᔇᒄ∄
// LeetCode, Minimum Path Sum
// ึᔇᒄ∄
class Solution {
public:
int minPathSum(vector<vector<int> > &grid) {
const int m = grid.size();
const int n = grid[0].size();
this->f = vector<vector<int> >(m, vector<int>(n, -1));
return dfs(grid, m-1, n-1);
}
private:
vector<vector<int> > f;
// 㑂ႇ
int dfs(const vector<vector<int> > &grid, int x, int y) {
if (x < 0 || y < 0) return INT_MAX; // 䊹⩻喌㏷ₑᲐХ喌∗ᘾ喌̼᭞0
if (x == 0 && y == 0) return grid[0][0]; // ఍ݟ䊦◨喌ᩥ᪊ᲐХ
return min(getOrUpdate(grid, x - 1, y),
getOrUpdate(grid, x, y - 1)) + grid[x][y];
}
int getOrUpdate(const vector<vector<int> > &grid, int x, int y) {
if (x < 0 || y < 0) return INT_MAX; // 䊹⩻喌∗ᘾ喌̼᭞0
if (f[x][y] >= 0) return f[x][y];
else return f[x][y] = dfs(grid, x, y);
}
};
ߗ㻳
// LeetCode, Minimum Path Sum
// λ㐣ߗ㻳
class Solution {
public:
int minPathSum(vector<vector<int> > &grid) {
if (grid.size() == 0) return 0;
const int m = grid.size();
const int n = grid[0].size();
int f[m][n];
f[0][0] = grid[0][0];
for (int i = 1; i < m; i++) {
f[i][0] = f[i - 1][0] + grid[i][0];
}
for (int i = 1; i < n; i++) {
f[0][i] = f[0][i - 1] + grid[0][i];

---

224
せ13 』
ߗᔰ㻳݁
}
for (int i = 1; i < m; i++) {
for (int j = 1; j < n; j++) {
f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j];
}
}
return f[m - 1][n - 1];
}
};
ߗ㻳+ ␉ߗ᪟㏳
// LeetCode, Minimum Path Sum
// λ㐣ߗ㻳+ ␉ߗ᪟㏳
class Solution {
public:
int minPathSum(vector<vector<int> > &grid) {
const int m = grid.size();
const int n = grid[0].size();
int f[n];
fill(f, f+n, INT_MAX); // ݌໺ի᭞INT_MAX喌ఏͩऽ䲑⩗ε min ܬ᪟ȡ
f[0] = 0;
for (int i = 0; i < m; i++) {
f[0] += grid[i][0];
for (int j = 1; j < n; j++) {
// ጕ䓨⮳f[j]喌㶗⹩ᰣ᫟ऽ⮳f[j]喌̽ڛᐾ͜⮳f[i[[j] ᄨᏃ
// ढ䓨⮳f[j]喌㶗⹩㔰⮳f[j]喌̽ڛᐾ͜⮳f[i-1][j] ᄨᏃ
f[j] = min(f[j - 1], f[j]) + grid[i][j];
}
}
return f[n - 1];
}
};
Ⱗڢ题Ⱍ
• Unique Paths, 㻰§10.2
• Unique Paths II, 㻰§10.3
13.9
Edit Distance
᣾䔟
Given two words word1 and word2, find the minimum number of steps required to convert word1 to
word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

---

13.9
Edit Distance
225
• Insert a character
• Delete a character
• Replace a character
ܵᲿ
䃭⟥ᔰͩ f[i][j]喌㶗⹩A[0,i] ঻B[0,j] ͺ䬣⮳ᰯᄾ㑅䓀䌌⻪ȡ䃭A[0,i] ⮳ᒑᐾ᭞str1c喌
B[0,j] ⮳ᒑᐾ᭞str2d喌
1. ັ᳋c==d喌݈f[i][j]=f[i-1][j-1]喛
2. ັ᳋c!=d喌
(a) ັ᳋ᄵc ᰮᢑ᜿d喌݈f[i][j]=f[i-1][j-1]+1喛
(b) ັ᳋౗c ऽ䲑〉ߏ̯͙ d喌݈f[i][j]=f[i][j-1]+1喛
(c) ັ᳋ᄵc ݏ䮓喌݈f[i][j]=f[i-1][j]+1喛
ߗ㻳
// LeetCode, Edit Distance
// λ㐣ߗ㻳喌ᬥ䬣฼ᱱᏕO(n*m)喌⾩䬣฼ᱱᏕO(n*m)
class Solution {
public:
int minDistance(const string &word1, const string &word2) {
const size_t n = word1.size();
const size_t m = word2.size();
// 䪮Ꮥͩ n ⮳ႆさ͡喌᰸n+1 ͙䯃Ხ
int f[n + 1][m + 1];
for (size_t i = 0; i <= n; i++)
f[i][0] = i;
for (size_t j = 0; j <= m; j++)
f[0][j] = j;
for (size_t i = 1; i <= n; i++) {
for (size_t j = 1; j <= m; j++) {
if (word1[i - 1] == word2[j - 1])
f[i][j] = f[i - 1][j - 1];
else {
int mn = min(f[i - 1][j], f[i][j - 1]);
f[i][j] = 1 + min(f[i - 1][j - 1], mn);
}
}
}
return f[n][m];
}
};

---

226
せ13 』
ߗᔰ㻳݁
ߗ㻳+ ␉ߗ᪟㏳
// LeetCode, Edit Distance
// λ㐣ߗ㻳+ ␉ߗ᪟㏳
// ᬥ䬣฼ᱱᏕO(n*m)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int minDistance(const string &word1, const string &word2) {
if (word1.length() < word2.length())
return minDistance(word2, word1);
int f[word2.length() + 1];
int upper_left = 0; // ䷌ๅ⩗̯͙इ䛾䃟ᒄf[i-1][j-1]
for (size_t i = 0; i <= word2.size(); ++i)
f[i] = i;
for (size_t i = 1; i <= word1.size(); ++i) {
upper_left = f[0];
f[0] = i;
for (size_t j = 1; j <= word2.size(); ++j) {
int upper = f[j];
if (word1[i - 1] == word2[j - 1])
f[j] = upper_left;
else
f[j] = 1 + min(upper_left, min(f[j], f[j - 1]));
upper_left = upper;
}
}
return f[word2.length()];
}
};
Ⱗڢ题Ⱍ
• ᬏ
13.10
Decode Ways
᣾䔟
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26

---

13.11
Distinct Subsequences
227
Given an encoded message containing digits, determine the total number of ways to decode it.
For example, Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2.
ܵᲿ
䌎Climbing Stairs (㻰§2.1.18) ᒷㆪѫ喌̼䓶้ߏ̯ϊݓ᫜䕪䓀ȡ
Вⴰ
// LeetCode, Decode Ways
// ߗ㻳喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int numDecodings(const string &s) {
if (s.empty() || s[0] == '0') return 0;
int prev = 0;
int cur = 1;
// 䪮Ꮥͩ n ⮳ႆさ͡喌᰸n+1 ͙䭥ᷞ
for (size_t i = 1; i <= s.size(); ++i) {
if (s[i-1] == '0') cur = 0;
if (i < 2 || !(s[i - 2] == '1' ||
(s[i - 2] == '2' && s[i - 1] <= '6')))
prev = 0;
int tmp = cur;
cur = prev + cur;
prev = tmp;
}
return cur;
}
};
Ⱗڢ题Ⱍ
• Climbing Stairs, 㻰§2.1.18
13.11
Distinct Subsequences
᣾䔟
Given a string S and a string T, count the number of distinct subsequences of T in S.
A subsequence of a string is a new string which is formed from the original string by deleting some (can
be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is
a subsequence of "ABCDE" while "AEC" is not).

---

228
せ13 』
ߗᔰ㻳݁
Here is an example: S = "rabbbit", T = "rabbit"
Return 3.
ܵᲿ
䃭⟥ᔰͩ f(i, j)喌㶗⹩T[0,j] ౗S[0,i] 䛻ܩ⣟⮳⁐᪟ȡ仅ٷ喌ᬏ䃩S[i] ঻T[j] ᭞ॕⰧ
へ喌㠔̼Ү⩗S[i]喌݈f(i, j) = f(i −1, j)喛㠔S[i]==T[j]喌݈ञДҮ⩗S[i]喌ₓᬥf(i, j) =
f(i −1, j) + f(i −1, j −1)ȡ
Вⴰ
// LeetCode, Distinct Subsequences
// λ㐣ߗ㻳+ ␉ߗ᪟㏳
// ᬥ䬣฼ᱱᏕO(m*n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int numDistinct(const string &S, const string &T) {
vector<int> f(T.size() + 1);
f[0] = 1;
for (int i = 0; i < S.size(); ++i) {
for (int j = T.size() - 1; j >= 0; --j) {
f[j + 1] += S[i] == T[j] ? f[j] : 0;
}
}
return f[T.size()];
}
};
Ⱗڢ题Ⱍ
• ᬏ
13.12
Word Break
᣾䔟
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.
For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".

---

13.12
Word Break
229
ܵᲿ
䃭⟥ᔰͩ f(i)喌㶗⹩s[0,i] ᭞ॕञДܵ䃼喌݈⟥ᔰ䒛⼪᫨⼺ͩ
f(i) = any_of(f(j)&&s[j + 1, i] ∈dict), 0 ≤j < i
⌠᥋
// LeetCode, Word Break
// ⌠᥋喌䊴ᬥ
// ᬥ䬣฼ᱱᏕO(2^n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
bool wordBreak(string s, unordered_set<string> &dict) {
return dfs(s, dict, 0, 0);
}
private:
static bool dfs(const string &s, unordered_set<string> &dict,
size_t start, size_t cur) {
if (cur == s.size()) {
return dict.find(s.substr(start, cur-start+1)) != dict.end();
}
if (dfs(s, dict, start, cur+1)) return true;
if (dict.find(s.substr(start, cur-start+1)) != dict.end())
if (dfs(s, dict, cur+1, cur+1)) return true;
return false;
}
};
ߗ㻳
// LeetCode, Word Break
// ߗ㻳喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
bool wordBreak(string s, unordered_set<string> &dict) {
// 䪮Ꮥͩ n ⮳ႆさ͡᰸n+1 ͙䯃Ხ
vector<bool> f(s.size() + 1, false);
f[0] = true; // ⾩ႆさ͡
for (int i = 1; i <= s.size(); ++i) {
for (int j = i - 1; j >= 0; --j) {
if (f[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
f[i] = true;
break;
}
}
}
return f[s.size()];
}
};

---

230
せ13 』
ߗᔰ㻳݁
Ⱗڢ题Ⱍ
• Word Break II, 㻰§13.13
13.13
Word Break II
᣾䔟
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word
is a valid dictionary word.
Return all such possible sentences.
For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].
ܵᲿ
౗̹̯题⮳ഩⵯ̹喌㺰䔃఍解ᱛ䏚ȡ
Вⴰ
// LeetCode, Word Break II
// ߗ㻳喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
vector<string> wordBreak(string s, unordered_set<string> &dict) {
// 䪮Ꮥͩ n ⮳ႆさ͡᰸n+1 ͙䯃Ხ
vector<bool> f(s.length() + 1, false);
// prev[i][j] ͩ true喌㶗⹩s[j, i) ᭞̯͙ष∄ࢄ䃼喌ञДϽ j ำܶᐯ
// せ̯㵻᱙⩗
vector<vector<bool> > prev(s.length() + 1, vector<bool>(s.length()));
f[0] = true;
for (size_t i = 1; i <= s.length(); ++i) {
for (int j = i - 1; j >= 0; --j) {
if (f[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
f[i] = true;
prev[i][j] = true;
}
}
}
vector<string> result;
vector<string> path;
gen_path(s, prev, s.length(), path, result);
return result;
}

---

13.13
Word Break II
231
private:
// DFS 䕼ࢵᵀ喌⩎᜿䌞ᒳ
void gen_path(const string &s, const vector<vector<bool> > &prev,
int cur, vector<string> &path, vector<string> &result) {
if (cur == 0) {
string tmp;
for (auto iter = path.crbegin(); iter != path.crend(); ++iter)
tmp += *iter + " ";
tmp.erase(tmp.end() - 1);
result.push_back(tmp);
}
for (size_t i = 0; i < s.size(); ++i) {
if (prev[cur][i]) {
path.push_back(s.substr(i, cur - i));
gen_path(s, prev, i, path, result);
path.pop_back();
}
}
}
};
Ⱗڢ题Ⱍ
• Word Break, 㻰§13.12

---

せ14 』
భ
ᬏीభ⮳㞱◨჉͸ັ̺喚
// ᬏीభ⮳㞱◨
struct UndirectedGraphNode {
int label;
vector<UndirectedGraphNode *> neighbors;
UndirectedGraphNode(int x) : label(x) {};
};
14.1
Clone Graph
᣾䔟
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbours.
OJ’s undirected graph serialization: Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbour of the
node. As an example, consider the serialized graph {0,1,2#1,2#2,2}.
The graph has a total of three nodes, and therefore contains three parts as separated by #.
1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
2. Second node is labeled as 1. Connect node 1 to node 2.
3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:
1
/ \
/
\
0 --- 2
/ \
\_/
ܵᲿ
ᎮᏕчٷ䕼ࢵᝅ⌠Ꮥчٷ䕼ࢵ䘬ञДȡ
232

---

14.1
Clone Graph
233
DFS
// LeetCode, Clone Graph
// DFS喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
UndirectedGraphNode *cloneGraph(const UndirectedGraphNode *node) {
if(node == nullptr) return nullptr;
// key is original node喌value is copied node
unordered_map<const UndirectedGraphNode *,
UndirectedGraphNode *> copied;
clone(node, copied);
return copied[node];
}
private:
// DFS
static UndirectedGraphNode* clone(const UndirectedGraphNode *node,
unordered_map<const UndirectedGraphNode *,
UndirectedGraphNode *> &copied) {
// a copy already exists
if (copied.find(node) != copied.end()) return copied[node];
UndirectedGraphNode *new_node = new UndirectedGraphNode(node->label);
copied[node] = new_node;
for (auto nbr : node->neighbors)
new_node->neighbors.push_back(clone(nbr, copied));
return new_node;
}
};
BFS
// LeetCode, Clone Graph
// BFS喌ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
UndirectedGraphNode *cloneGraph(const UndirectedGraphNode *node) {
if (node == nullptr) return nullptr;
// key is original node喌value is copied node
unordered_map<const UndirectedGraphNode *,
UndirectedGraphNode *> copied;
// each node in queue is already copied itself
// but neighbors are not copied yet
queue<const UndirectedGraphNode *> q;
q.push(node);
copied[node] = new UndirectedGraphNode(node->label);
while (!q.empty()) {
const UndirectedGraphNode *cur = q.front();
q.pop();
for (auto nbr : cur->neighbors) {
// a copy already exists
if (copied.find(nbr) != copied.end()) {
copied[cur]->neighbors.push_back(copied[nbr]);

---

234
せ14 』
భ
} else {
UndirectedGraphNode *new_node =
new UndirectedGraphNode(nbr->label);
copied[nbr] = new_node;
copied[cur]->neighbors.push_back(new_node);
q.push(nbr);
}
}
}
return copied[node];
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

せ15 』
㏵㞱Ⴭ⣟题
䔈ㆪ题Ⱍ̼㔲➨჉⮳テ∄喌㏞㇨㔲ᄎۈВⴰ⮳⛎㏲Ꮥȡ
15.1
Reverse Integer
᣾䔟
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought
through this!
If the integer’s last digit is 0, what should the output be? ie, cases such as 10, 100.
Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the
reverse of 1000000003 overflows. How should you handle such cases?
Throw an exception? Good, but what if throwing an exception is not an option? You would then have
to re-design the function (ie, add an extra parameter).
ܵᲿ
ⴜᄾ㇭ᖼ⮳题喌ВⴰΎञДۈ⮳ᒷⴜᄾȡ
Вⴰ
//LeetCode, Reverse Integer
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
// 㔲㮀1. 䉎᪟⮳ᗴۤ 2. ⏑ܩ⮳ᗴۤ (ₒ⏑ܩ&& 䉎⏑ܩ喌℃ັx = -2147483648(ࢢ-2^31) )
class Solution {
public:
int reverse (int x) {
long long r = 0;
long long t = x;
t = t > 0 ? t : -t;
235

---

236
せ15 』
㏵㞱Ⴭ⣟题
for (; t; t /= 10)
r = r * 10 + t % 10;
bool sign = x > 0 ? false: true;
if (r > 2147483647 || (sign && r > 2147483648)) {
return 0;
} else {
if (sign) {
return -r;
} else {
return r;
}
}
}
};
Ⱗڢ题Ⱍ
• Palindrome Number, 㻰§15.2
15.2
Palindrome Number
᣾䔟
Determine whether an integer is a palindrome. Do this without extra space.
Some hints:
Could negative integers be palindromes? (ie, -1)
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem ”Reverse Integer”,
you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.
ܵᲿ
仅ٷᘢݟ喌ञДݘ⩗̹̯题喌ᄵ᪣᪟ࣼ䒛喌♥ऽ̽࣎Ე⮳᪣᪟℃䒲喌᭞ॕⰧへ喌Ⱗへ݈ͩ Palindrome
⮳ȡञ᭞reverse() щ⏑ܩȡ
ₒ⶝⮳解∄᭞喌̼᫜౟अせ̯Ѽ঻ᰯऽ̯Ѽ喈10 䔊ݥ̺喉䔊㵻℃䒲喌Ⱗへ݈अせλѼ঻Ձ᪟せ
λѼ喌ⰣݟႻ᜿℃䒲ᝅ㔴͜䕃ឭݟε̼̯㜣⮳Ѽȡ
Вⴰ
//LeetCode, Palindrome Number
// ᬥ䬣฼ᱱᏕO(1)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:

---

15.3
Insert Interval
237
bool isPalindrome(int x) {
if (x < 0) return false;
int d = 1; // divisor
while (x / d >= 10) d *= 10;
while (x > 0) {
int q = x / d;
// quotient
int r = x % 10;
// remainder
if (q != r) return false;
x = x % d / 10;
d /= 100;
}
return true;
}
};
Ⱗڢ题Ⱍ
• Reverse Integer, 㻰§15.1
• Valid Palindrome, 㻰§3.1
15.3
Insert Interval
᣾䔟
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1: Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16],
insert and merge [4,9] in as
[1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
ܵᲿ
ᬏ
Вⴰ
struct Interval {
int start;
int end;
Interval() : start(0), end(0) { }
Interval(int s, int e) : start(s), end(e) { }
};
//LeetCode, Insert Interval

---

238
せ15 』
㏵㞱Ⴭ⣟题
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
vector<Interval>::iterator it = intervals.begin();
while (it != intervals.end()) {
if (newInterval.end < it->start) {
intervals.insert(it, newInterval);
return intervals;
} else if (newInterval.start > it->end) {
it++;
continue;
} else {
newInterval.start = min(newInterval.start, it->start);
newInterval.end = max(newInterval.end, it->end);
it = intervals.erase(it);
}
}
intervals.insert(intervals.end(), newInterval);
return intervals;
}
};
Ⱗڢ题Ⱍ
• Merge Intervals喌㻰§15.4
15.4
Merge Intervals
᣾䔟
Given a collection of intervals, merge all overlapping intervals.
For example, Given [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18]
ܵᲿ
฼⩗̯̺ Insert Intervals ⮳解∄ࢢञ喌݊ᐩ̯͙᫟⮳interval 䯵ष喌♥ऽ⃾⁐Ͻᬖ⮳䛻䲑अ̯͙
interval ܩᲔ喌♥ऽᤁڔݟ᫟⮳䯵ष͜ȡ
Вⴰ
struct Interval {
int start;
int end;
Interval() : start(0), end(0) { }
Interval(int s, int e) : start(s), end(e) { }
};

---

15.5
Minimum Window Substring
239
//LeetCode, Merge Interval
//฼⩗̯̺ Insert Intervals ⮳解∄ࢢञ
// ᬥ䬣฼ᱱᏕO(n1+n2+...)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<Interval> merge(vector<Interval> &intervals) {
vector<Interval> result;
for (int i = 0; i < intervals.size(); i++) {
insert(result, intervals[i]);
}
return result;
}
private:
vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
vector<Interval>::iterator it = intervals.begin();
while (it != intervals.end()) {
if (newInterval.end < it->start) {
intervals.insert(it, newInterval);
return intervals;
} else if (newInterval.start > it->end) {
it++;
continue;
} else {
newInterval.start = min(newInterval.start, it->start);
newInterval.end = max(newInterval.end, it->end);
it = intervals.erase(it);
}
}
intervals.insert(intervals.end(), newInterval);
return intervals;
}
};
Ⱗڢ题Ⱍ
• Insert Interval喌㻰§15.3
15.5
Minimum Window Substring
᣾䔟
Given a string S and a string T, find the minimum window in S which will contain all the characters in
T in complexity O(n).
For example, S = "ADOBECODEBANC", T = "ABC"
Minimum window is "BANC".
Note:
• If there is no such window in S that covers all characters in T, return the emtpy string "".

---

240
せ15 』
㏵㞱Ⴭ⣟题
• If there are multiple such windows, you are guaranteed that there will always be only one unique
minimum window in S.
ܵᲿ
ࣻᠶ䦷喌ߗᔰ㐣៓̯͙ࡩ䬣ȡᅭᠶ䦷̼᫜ᒯऽរ喌ᒂរݟ᰸̯͙⿆ऒ࠴ग़εᝯ᰸T ⮳ႆさऽ喌♥
ऽڼᩥ㑘๣ᠶ䦷喌Ⱓݟ̼㘬ڼᩥ㑘ͩₑȡᰯऽ䃟ᒄᝯ᰸ञ㘬⮳ᗴۤ͜⿆ऒᰯᄾ⮳
Вⴰ
// LeetCode, Minimum Window Substring
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
string minWindow(string S, string T) {
if (S.empty()) return "";
if (S.size() < T.size()) return "";
const int ASCII_MAX = 256;
int appeared_count[ASCII_MAX];
int expected_count[ASCII_MAX];
fill(appeared_count, appeared_count + ASCII_MAX, 0);
fill(expected_count, expected_count + ASCII_MAX, 0);
for (size_t i = 0; i < T.size(); i++) expected_count[T[i]]++;
int minWidth = INT_MAX, min_start = 0;
// ⿆ऒ๖ᄾ喌䊦◨
int wnd_start = 0;
int appeared = 0;
// Ⴛ᪣࠴ग़ε̯͙ T
//ᅭᠶ䦷̼᫜ᒯऽរ
for (size_t wnd_end = 0; wnd_end < S.size(); wnd_end++) {
if (expected_count[S[wnd_end]] > 0)
{
// this char is a part of T
appeared_count[S[wnd_end]]++;
if (appeared_count[S[wnd_end]] <= expected_count[S[wnd_end]])
appeared++;
}
if (appeared == T.size()) {
// Ⴛ᪣࠴ग़ε̯͙ T
// ᩥ㑘๣ᠶ䦷
while (appeared_count[S[wnd_start]] > expected_count[S[wnd_start]]
|| expected_count[S[wnd_start]] == 0) {
appeared_count[S[wnd_start]]--;
wnd_start++;
}
if (minWidth > (wnd_end - wnd_start + 1)) {
minWidth = wnd_end - wnd_start + 1;
min_start = wnd_start;
}
}
}
if (minWidth == INT_MAX) return "";

---

15.6
Multiply Strings
241
else return S.substr(min_start, minWidth);
}
};
Ⱗڢ题Ⱍ
• ᬏ
15.6
Multiply Strings
᣾䔟
Given two numbers represented as strings, return multiplication of the numbers as a string.
Note: The numbers can be arbitrarily large and are non-negative.
ܵᲿ
倇㇭Ꮥ·∄ȡ
፧㻰⮳։∄᭞ᄵႆさ䒛ࡅ̯͙ͩ int喌̯̯ᄨᏃ喌ᒑ᜿̯͙ int ᪟㏳ȡѵ᭞䔈ᵦᒷ⊙䉨⾩䬣喌̯͙
int32 ⮳ᰯ๖ի᭞231 −1 = 2147483647喌ञД̽ 9 ͙ႆさᄨᏃ喌⩠ν᰸·∄喌۾ࡹ喌݈㜢ᅀञД̽
4 ͙ႆさ̯̯ᄨᏃȡ̯͙ int64 ञД̽ 9 ͙ႆさᄨᏃȡ
Вⴰ1
// LeetCode, Multiply Strings
// @author 䔍೽(http://weibo.com/lianchengzju)
// ̯͙ႆさᄨᏃ̯͙ int
// ᬥ䬣฼ᱱᏕO(n*m)喌⾩䬣฼ᱱᏕO(n+m)
typedef vector<int> bigint;
bigint make_bigint(string const& repr) {
bigint n;
transform(repr.rbegin(), repr.rend(), back_inserter(n),
[](char c) { return c - '0'; });
return n;
}
string to_string(bigint const& n) {
string str;
transform(find_if(n.rbegin(), prev(n.rend()),
[](char c) { return c > '\0'; }), n.rend(), back_inserter(str),
[](char c) { return c + '0'; });
return str;
}
bigint operator*(bigint const& x, bigint const& y) {
bigint z(x.size() + y.size());

---

242
せ15 』
㏵㞱Ⴭ⣟题
for (size_t i = 0; i < x.size(); ++i)
for (size_t j = 0; j < y.size(); ++j) {
z[i + j] += x[i] * y[j];
z[i + j + 1] += z[i + j] / 10;
z[i + j] %= 10;
}
return z;
}
class Solution {
public:
string multiply(string num1, string num2) {
return to_string(make_bigint(num1) * make_bigint(num2));
}
};
Вⴰ2
// LeetCode, Multiply Strings
// 9 ͙ႆさᄨᏃ̯͙ int64_t
// ᬥ䬣฼ᱱᏕO(n*m/81)喌⾩䬣฼ᱱᏕO((n+m)/9)
/** ๖᪣᪟ㆪ. */
class BigInt {
public:
/**
* @brief Ჳ䕏ܬ᪟喌ᄵႆさ͡䒛ࡅͩ๖᪣᪟.
* @param[in] s 䓂ڔ⮳ႆさ͡
* @return ᬏ
*/
BigInt(string s) {
vector<int64_t> result;
result.reserve(s.size() / RADIX_LEN + 1);
for (int i = s.size(); i > 0; i -= RADIX_LEN) {
// [i-RADIX_LEN, i)
int temp = 0;
const int low = max(i - RADIX_LEN, 0);
for (int j = low; j < i; j++) {
temp = temp * 10 + s[j] - '0';
}
result.push_back(temp);
}
elems = result;
}
/**
* @brief ᄵ᪣᪟䒛ࡅͩႆさ͡.
* @return ႆさ͡
*/
string toString() {
stringstream result;
bool started = false; // ⩗ν䌢䓶ݼᄫ0
for (auto i = elems.rbegin(); i != elems.rend(); i++) {

---

15.6
Multiply Strings
243
if (started) { // ັ᳋้҈⮳0 ጡ㏾䘬䌢䓶喌݈䓂ܩ
result << setw(RADIX_LEN) << setfill('0') << *i;
} else {
result << *i;
started = true; // ⷟ݟせ̯͙䲍0 ⮳ի喌ᅠ䄣ᬽ้҈⮳0 ጡ㏾䘬䌢䓶
}
}
if (!started) return "0"; // ᒂx ڗͩ 0 ᬥ
else return result.str();
}
/**
* @brief ๖᪣᪟·∄.
* @param[in] x x
* @param[in] y y
* @return ๖᪣᪟
*/
static BigInt multiply(const BigInt &x, const BigInt &y) {
vector<int64_t> z(x.elems.size() + y.elems.size(), 0);
for (size_t i = 0; i < y.elems.size(); i++) {
for (size_t j = 0; j < x.elems.size(); j++) { // ⩗y[i] ࣪·Д x ⮳ळѼ
//
͓᪟せi, j ѼⰧ·喌㉞ߏݟ㐂᳋⮳せi+j Ѽ
z[i + j] += y.elems[i] * x.elems[j];
if (z[i + j] >= BIGINT_RADIX) { //
ⰺ᭞ॕ㺰䔊Ѽ
z[i + j + 1] += z[i + j] / BIGINT_RADIX; //
䔊Ѽ
z[i + j] %= BIGINT_RADIX;
}
}
}
while (z.back() == 0) z.pop_back();
// ⇐᰸䔊Ѽ喌࣪ᢸᰯ倇Ѽ⮳0
return BigInt(z);
}
private:
typedef long long int64_t;
/** ̯͙᪟㏳ٲ㉏ᄨᏃ9 ͙ࡰ䔊ݥѼ喌ࢢ᪟㏳᭞Ϯ䔊ݥ⮳
* ఏͩ 1000000000 * 1000000000 ⇐᰸䊴䓶2^63-1
*/
const static int BIGINT_RADIX = 1000000000;
const static int RADIX_LEN = 9;
/** ̶䔊ݥ᪣᪟. */
vector<int64_t> elems;
BigInt(const vector<int64_t> num) : elems(num) {}
};
class Solution {
public:
string multiply(string num1, string num2) {
BigInt x(num1);

---

244
せ15 』
㏵㞱Ⴭ⣟题
BigInt y(num2);
return BigInt::multiply(x, y).toString();
}
};
Ⱗڢ题Ⱍ
• ᬏ
15.7
Substring with Concatenation of All Words
᣾䔟
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of
substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].(order does not matter).
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Substring with Concatenation of All Words
// ᬥ䬣฼ᱱᏕO(n*m)喌⾩䬣฼ᱱᏕO(m)
class Solution {
public:
vector<int> findSubstring(string s, vector<string>& dict) {
size_t wordLength = dict.front().length();
size_t catLength = wordLength * dict.size();
vector<int> result;
if (s.length() < catLength) return result;
unordered_map<string, int> wordCount;
for (auto const& word : dict) ++wordCount[word];
for (auto i = begin(s); i <= prev(end(s), catLength); ++i) {
unordered_map<string, int> unused(wordCount);
for (auto j = i; j != next(i, catLength); j += wordLength) {
auto pos = unused.find(string(j, next(j, wordLength)));

---

15.8
Pascal’s Triangle
245
if (pos == unused.end() || pos->second == 0) break;
if (--pos->second == 0) unused.erase(pos);
}
if (unused.size() == 0) result.push_back(distance(begin(s), i));
}
return result;
}
};
Ⱗڢ题Ⱍ
• ᬏ
15.8
Pascal’s Triangle
᣾䔟
Given numRows, generate the first numRows of Pascal’s triangle.
For example, given numRows = 5,
Return
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
ܵᲿ
ᱛ题ञД⩗䭎݆喌䃐テ̺̯㵻ᬥ喌㐈̹̯㵻ጕढळߏ̯͙ 0喌♥ऽ̺̯㵻⮳⃾͙ٲ㉏喌ᅠへνጕ
̹㼁঻ढ̹㼁ͺ঻ȡ
क̯⻼ᕌ䌞喌̺̯㵻せ̯͙ٲ㉏঻ᰯऽ̯͙ٲ㉏䉺իͩ 1喌͜䬣⮳⃾͙ٲ㉏喌へν̹̯㵻⮳ጕ̹
㼁঻ढ̹㼁ٲ㉏ͺ঻ȡ
Ͻጕݟढ
// LeetCode, Pascal's Triangle
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > generate(int numRows) {
vector<vector<int> > result;

---

246
せ15 』
㏵㞱Ⴭ⣟题
if(numRows == 0) return result;
result.push_back(vector<int>(1,1)); //first row
for(int i = 2; i <= numRows; ++i) {
vector<int> current(i,1);
// ᱛ㵻
const vector<int> &prev = result[i-2];
// ̹̯㵻
for(int j = 1; j < i - 1; ++j) {
current[j] = prev[j-1] + prev[j]; // ጕ̹㼁঻ढ̹㼁ͺ঻
}
result.push_back(current);
}
return result;
}
};
Ͻढݟጕ
// LeetCode, Pascal's Triangle
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<vector<int> > generate(int numRows) {
vector<vector<int> > result;
vector<int> array;
for (int i = 1; i <= numRows; i++) {
for (int j = i - 2; j > 0; j--) {
array[j] = array[j - 1] + array[j];
}
array.push_back(1);
result.push_back(array);
}
return result;
}
};
Ⱗڢ题Ⱍ
• Pascal’s Triangle II喌㻰§15.9
15.9
Pascal’s Triangle II
᣾䔟
Given an index k, return the kth row of the Pascal’s triangle.
For example, given k = 3,
Return [1,3,3,1].
Note: Could you optimize your algorithm to use only O(k) extra space?

---

15.10
Spiral Matrix
247
ܵᲿ
␉ߗ᪟㏳ȡ
Вⴰ
// LeetCode, Pascal's Triangle II
// ␉ߗ᪟㏳喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
vector<int> getRow(int rowIndex) {
vector<int> array;
for (int i = 0; i <= rowIndex; i++) {
for (int j = i - 1; j > 0; j--){
array[j] = array[j - 1] + array[j];
}
array.push_back(1);
}
return array;
}
};
Ⱗڢ题Ⱍ
• Pascal’s Triangle喌㻰§15.8
15.10
Spiral Matrix
᣾䔟
Given a matrix of m×n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example, Given the following matrix:
[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
ܵᲿ
ὐ᠎ȡ

---

248
せ15 』
㏵㞱Ⴭ⣟题
Вⴰ
// LeetCode, Spiral Matrix
// @author 哉䭵Ⴘ(http://weibo.com/luangong)
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<int> spiralOrder(vector<vector<int> >& matrix) {
vector<int> result;
if (matrix.empty()) return result;
int beginX = 0, endX = matrix[0].size() - 1;
int beginY = 0, endY = matrix.size() - 1;
while (true) {
// From left to right
for (int j = beginX; j <= endX; ++j) result.push_back(matrix[beginY][j]);
if (++beginY > endY) break;
// From top to bottom
for (int i = beginY; i <= endY; ++i) result.push_back(matrix[i][endX]);
if (beginX > --endX) break;
// From right to left
for (int j = endX; j >= beginX; --j) result.push_back(matrix[endY][j]);
if (beginY > --endY) break;
// From bottom to top
for (int i = endY; i >= beginY; --i) result.push_back(matrix[i][beginX]);
if (++beginX > endX) break;
}
return result;
}
};
Ⱗڢ题Ⱍ
• Spiral Matrix II 喌㻰§15.11
15.11
Spiral Matrix II
᣾䔟
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example, Given n = 3,
You should return the following matrix:
[
[ 1, 2, 3 ],
[ 8, 9, 4 ],
[ 7, 6, 5 ]
]

---

15.11
Spiral Matrix II
249
ܵᲿ
䔈题℃̹̯题㺰クࢄȡ
Вⴰ1
// LeetCode, Spiral Matrix II
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
vector<vector<int> > generateMatrix(int n) {
vector<vector<int> > matrix(n, vector<int>(n));
int begin = 0, end = n - 1;
int num = 1;
while (begin < end) {
for (int j = begin; j < end; ++j) matrix[begin][j] = num++;
for (int i = begin; i < end; ++i) matrix[i][end] = num++;
for (int j = end; j > begin; --j) matrix[end][j] = num++;
for (int i = end; i > begin; --i) matrix[i][begin] = num++;
++begin;
--end;
}
if (begin == end) matrix[begin][begin] = num;
return matrix;
}
};
Вⴰ2
// LeetCode, Spiral Matrix II
// @author 哉䭵Ⴘ(http://weibo.com/luangong)
// ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n^2)
class Solution {
public:
vector<vector<int> > generateMatrix(int n) {
vector< vector<int> > matrix(n, vector<int>(n));
if (n == 0) return matrix;
int beginX = 0, endX = n - 1;
int beginY = 0, endY = n - 1;
int num = 1;
while (true) {
for (int j = beginX; j <= endX; ++j) matrix[beginY][j] = num++;
if (++beginY > endY) break;
for (int i = beginY; i <= endY; ++i) matrix[i][endX] = num++;
if (beginX > --endX) break;
for (int j = endX; j >= beginX; --j) matrix[endY][j] = num++;
if (beginY > --endY) break;

---

250
せ15 』
㏵㞱Ⴭ⣟题
for (int i = endY; i >= beginY; --i) matrix[i][beginX] = num++;
if (++beginX > endX) break;
}
return matrix;
}
};
Ⱗڢ题Ⱍ
• Spiral Matrix, 㻰§15.10
15.12
ZigZag Conversion
᣾䔟
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you
may want to display this pattern in a fixed font for better legibility)
P
A
H
N
A P L S I I G
Y
I
R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
ܵᲿ
㺰ឭݟ᪟႕㻳ᒺȡⱎₒ䲑䄄͜喌̼๖ञ㘬ܩ䔈⻼䬝题ȡ
n=4:
P
I
N
A
L S
I G
Y A
H R
P
I
n=5:
P
H
A
S I
Y
I
R
P L
I
G
A
N
ᝯД喌ᄨν⃾̯ᅱಱⰣٲ㉏⮳౿ᴶ(i, j) = (j + 1) ∗n + i喛ᄨν⃾͓ᅱಱⰣٲ㉏ͺ䬣⮳ᤁڔٲ
㉏喈᫋ᄨ㼁ٲ㉏喉喌(i, j) = (j + 1) ∗n −i

---

15.13
Divide Two Integers
251
Вⴰ
// LeetCode, ZigZag Conversion
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
string convert(string s, int nRows) {
if (nRows <= 1 || s.size() <= 1) return s;
string result;
for (int i = 0; i < nRows; i++) {
for (int j = 0, index = i; index < s.size();
j++, index = (2 * nRows - 2) * j + i) {
result.append(1, s[index]);
// ಱⰣٲ㉏
if (i == 0 || i == nRows - 1) continue;
// ᫋ᄨ㼁ٲ㉏
if (index + (nRows - i - 1) * 2 < s.size())
result.append(1, s[index + (nRows - i - 1) * 2]);
}
}
return result;
}
};
Ⱗڢ题Ⱍ
• ᬏ
15.13
Divide Two Integers
᣾䔟
Divide two integers without using multiplication, division and mod operator.
ܵᲿ
̼㘬⩗·Ƞ䮓঻अὐ喌䗒ޘ̺⮳喌䔇᰸ߏȠ۾঻Ѽ䓿テȡ
ᰯクࢄ⮳᫨∄喌᭞̼᫜۾࣪㷚䮓᪟ȡ౗䔈͙ഩⵯ̹喌ञД։̯◨чࡅ喌⃾⁐ឹ㷚䮓᪟㔪Լ喌Ͻ㔻
ߏ䕎ȡ
Вⴰ1
// LeetCode, Divide Two Integers
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int divide(int dividend, int divisor) {
// ᒂdividend = INT_MIN ᬥ喌-dividend щ⏑ܩ喌ᝯД⩗long long
long long a = dividend >= 0 ? dividend : -(long long)dividend;
long long b = divisor >= 0 ? divisor : -(long long)divisor;

---

252
せ15 』
㏵㞱Ⴭ⣟题
// ᒂdividend = INT_MIN ᬥ喌divisor = -1 ᬥ喌㐂᳋щ⏑ܩ喌ᝯД⩗long long
long long result = 0;
while (a >= b) {
long long c = b;
for (int i = 0; a >= c; ++i, c <<= 1) {
a -= c;
result += 1 << i;
}
}
return ((dividend^divisor) >> 31) ? (-result) : (result);
}
};
Вⴰ2
// LeetCode, Divide Two Integers
// ᬥ䬣฼ᱱᏕO(logn)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int divide(int dividend, int divisor) {
int result = 0; // ᒂdividend = INT_MIN ᬥ喌divisor = -1 ᬥ喌㐂᳋щ⏑ܩ
const bool sign = (dividend > 0 && divisor < 0) ||
(dividend < 0 && divisor > 0); // ᐱद
// ᒂdividend = INT_MIN ᬥ喌-dividend щ⏑ܩ喌ᝯД⩗unsigned int
unsigned int a = dividend >= 0 ? dividend : -dividend;
unsigned int b = divisor >= 0 ? divisor : -divisor;
while (a >= b) {
int multi = 1;
unsigned int bb = b;
while (a >= bb) {
a -= bb;
result += multi;
if (bb < INT_MAX >> 1) { // 䭡ₑ⏑ܩ
bb += bb;
multi += multi;
}
}
}
if (sign) return -result;
else return result;
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

15.14
Text Justification
253
15.14
Text Justification
᣾䔟
Given an array of words and a length L, format the text such that each line has exactly L characters and
is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a
line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the
slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
"This
is
an",
"example
of text",
"justification.
"
]
Note: Each word is guaranteed not to exceed L in length.
Corner Cases:
• A line other than the last line might contain only one word. What should you do in this case?
• In this case, that line should be left
ܵᲿ
ᬏ
Вⴰ
// LeetCode, Text Justification
// ᬥ䬣฼ᱱᏕO(n)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
vector<string> fullJustify(vector<string> &words, int L) {
vector<string> result;
const int n = words.size();
int begin = 0, len = 0; // ᒂݼ㵻⮳䊦◨喌ᒂݼ䪮Ꮥ
for (int i = 0; i < n; ++i) {
if (len + words[i].size() + (i - begin) > L) {
result.push_back(connect(words, begin, i - 1, len, L, false));

---

254
せ15 』
㏵㞱Ⴭ⣟题
begin = i;
len = 0;
}
len += words[i].size();
}
// ᰯऽ̯㵻̼䋢L
result.push_back(connect(words, begin, n - 1, len, L, true));
return result;
}
/**
* @brief ᄵwords[begin, end] 䔍᜿̯㵻
* @param[in] words ࢄ䃼݆㶗
* @param[in] begin ᐯ໺
* @param[in] end 㐂᲎
* @param[in] len words[begin, end] ᝯ᰸ࢄ䃼ߏ䊦Ე⮳䪮Ꮥ
* @param[in] L 题Ⱍ㻳჉⮳̯㵻䪮Ꮥ
* @param[in] is_last ᭞ॕ᭞ᰯऽ̯㵻
* @return ᄨ呿ऽ⮳ᒂݼ㵻
*/
string connect(vector<string> &words, int begin, int end,
int len, int L, bool is_last) {
string s;
int n = end - begin + 1;
for (int i = 0; i < n; ++i) {
s += words[begin + i];
addSpaces(s, i, n - 1, L - len, is_last);
}
if (s.size() < L) s.append(L - s.size(), ' ');
return s;
}
/**
* @brief 〉ߏ⾩ᵫ.
* @param[inout]s ̯㵻
* @param[in] i ᒂݼ⾩䯈⮳Ꮎद
* @param[in] n ⾩䯈ᕪ᪟
* @param[in] L ᕪڠ䰯㺰〉ߏ⮳⾩䷌᪟
* @param[in] is_last ᭞ॕ᭞ᰯऽ̯㵻
* @return ᬏ
*/
void addSpaces(string &s, int i, int n, int L, bool is_last) {
if (n < 1 || i > n - 1) return;
int spaces = is_last ? 1 : (L / n + (i < (L % n) ? 1 : 0));
s.append(spaces, ' ');
}
};
Ⱗڢ题Ⱍ
• ᬏ

---

15.15
Max Points on a Line
255
15.15
Max Points on a Line
᣾䔟
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
ܵᲿ
ᯣߊ᳉ͭ∄ȡ͓◨ۢ჉̯ᲐⰣ㏮喌n ͙◨͓͓㏳ष喌ञДᓆݟ1
2n(n + 1) ᲐⰣ㏮喌ᄨ⃾̯ᲐⰣ
㏮喌ݓ᫜n ͙◨᭞ॕ౗䄔Ⱓ㏮̹喌Ͻ㔻ञДᓆݟ䔈ᲐⰣ㏮̹⮳◨⮳͙᪟喌䔸᠘ᰯ๖⮳䗒ᲐⰣ㏮䔃఍ȡ
฼ᱱᏕO(n3)ȡ
̹䲑⮳ᯣߊ᳉ͭ∄ДĆ䓨ćͩ͜ᓲ喌ڼⰺक̯⻼ᯣߊ᳉ͭ∄喌Д⃾͙Ć◨ćͩ͜ᓲ喌♥ऽ䕼ࢵޘ
҈◨喌ឭݟᝯ᰸⮳᫋⢶喌ັ᳋᫋⢶Ⱗऻ喌䗒ͷ̯჉ڠ㏮ᄨ⃾͙◨喌⩗̯͙৷ጻ㶗喌key ͩ᫋⢶喌value
ͩ䄔Ⱓ㏮̹⮳◨᪟喌䃐テܩ৷ጻ㶗ऽ喌अᰯ๖ի喌Ꭵᰣ᫟ڗᅯᰯ๖ի喌ᰯऽᅠ᭞㐂᳋ȡᬥ䬣฼ᱱᏕ
O(n2)喌⾩䬣฼ᱱᏕO(n)ȡ
Д䓨ͩ͜ᓲ
// LeetCode, Max Points on a Line
// ᯣߊ᳉ͭ∄喌Д䓨ͩ͜ᓲ喌ᬥ䬣฼ᱱᏕO(n^3)喌⾩䬣฼ᱱᏕO(1)
class Solution {
public:
int maxPoints(vector<Point> &points) {
if (points.size() < 3) return points.size();
int result = 0;
for (int i = 0; i < points.size() - 1; i++) {
for (int j = i + 1; j < points.size(); j++) {
int sign = 0;
int a, b, c;
if (points[i].x == points[j].x) sign = 1;
else {
a = points[j].x - points[i].x;
b = points[j].y - points[i].y;
c = a * points[i].y - b * points[i].x;
}
int count = 0;
for (int k = 0; k < points.size(); k++) {
if ((0 == sign && a * points[k].y == c +
b * points[k].x) ||
(1 == sign&&points[k].x == points[j].x))
count++;
}
if (count > result) result = count;
}
}
return result;
}
};

---

256
せ15 』
㏵㞱Ⴭ⣟题
Д◨ͩ͜ᓲ
// LeetCode, Max Points on a Line
// ᯣߊ᳉ͭ喌Д◨ͩ͜ᓲ喌ᬥ䬣฼ᱱᏕO(n^2)喌⾩䬣฼ᱱᏕO(n)
class Solution {
public:
int maxPoints(vector<Point> &points) {
if (points.size() < 3) return points.size();
int result = 0;
unordered_map<double, int> slope_count;
for (int i = 0; i < points.size()-1; i++) {
slope_count.clear();
int samePointNum = 0; // ̽ i 䛼ष⮳◨
int point_max = 1;
// ঻i ڠ㏮⮳ᰯ๖◨᪟
for (int j = i + 1; j < points.size(); j++) {
double slope; // ᫋⢶
if (points[i].x == points[j].x) {
slope = std::numeric_limits<double>::infinity();
if (points[i].y == points[j].y) {
++ samePointNum;
continue;
}
} else {
slope = 1.0 * (points[i].y - points[j].y) /
(points[i].x - points[j].x);
}
int count = 0;
if (slope_count.find(slope) != slope_count.end())
count = ++slope_count[slope];
else {
count = 2;
slope_count[slope] = 2;
}
if (point_max < count) point_max = count;
}
result = max(result, point_max + samePointNum);
}
return result;
}
};
Ⱗڢ题Ⱍ
• ᬏ