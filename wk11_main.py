import turtle
import math
wn=turtle.Screen()

t1=turtle.Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()


def ring():

    ring = turtle.Turtle()
    ring.penup()
    ring.setpos(-300,300)
    ring.pendown()
    ring.pensize(3)

    #-300,300  ->  300,300  ->  300,-300  ->  -300,-300
    for side in range(4):
        ring.fd(600)
        ring.right(90)
        ring.write(ring.pos())
    ring.hideturtle()

    
    
def turnright():
    t1.right(45)

def turnleft():
    t1.left(45)

def keyup():
    t1.fd(100)
    
def turnback():
    t1.right(180)
    
def mousegoto(x,y):
    t1.setpos(x,y)
    feedback()
    

def keybye():
    wn.bye()


def addkeys():
    wn.onkey(turnright,"Right")
    wn.onkey(turnleft,"Left")
    wn.onkey(keyup,"Up")
    wn.onkey(turnback,"Down")
    wn.onkey(keybye,"q")

def addmouse():
    wn.onclick(mousegoto)

    
def feedback():
    if t1.xcor() > 300 or t1.xcor() < -300:
        t1.right(180)
        t1.write("On the line")

    if t1.ycor() > 300 or t1.ycor() < -300:
        t1.right(180)
        t1.write("On the line")

def schoolLife():
    survey = [["highly satisfactoty", "satisfaction", "dissatisfaction" ,"highly unsatisfactory"],
                [13.1, 37.1, 8.7, 1.5],
                [10.6, 34.6, 13.4, 1.9],
                [27.1, 40.0, 2.9, 1.5],
                [16.2, 37.8, 6.8, 0.8],
                [11.4, 29.8, 14.8, 4.9],
                [12.2, 26.5, 14.9, 4.4],
                [13.5, 29.7, 11.1, 2.4],
                [13.7, 37.6, 4.1, 1.2]]
    grade=survey[1:8]
    sSum=0
    dsSum=0
    
    for i in range(len(grade)):
        sSum = sSum + grade[i][0] + grade[i][1]
        dsSum = dsSum + grade[i][2] + grade[i][3]
        
    sAvg=sSum/len(grade)
    dsAvg=dsSum/len(grade)
    
    print "Average of (highly) Satisfaction:", sAvg
    print "Average of (highly) unsatisfactory :", dsAvg

    
def speech():
    Bush=["Vice President Cheney, Mr. Chief Justice, President Carter, President Bush, President Clinton, reverend clergy, distinguished guests, fellow citizens:",
        "On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country.", 
          "I am grateful for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed.",
        "At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century, America defended our own freedom by standing watch on distant borders.",
          "After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical —and then there came a day of fire.",
        "We have seen our vulnerability —and we have seen its deepest source. For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed hatred and excuse murder ",
          "— violence will gather, and multiply in destructive power, and cross the most defended borders, and raise a mortal threat. There is only one force of history that can break the reign of hatred and resentment,", 
          "and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human freedom.",
        "We are led, by events and common sense, to one conclusion: The survival of liberty in our land increasingly depends on the success of liberty in other lands. The best hope for peace in our world is the expansion of",
          "freedom in all the world.",
        "America's vital interests and our deepest beliefs are now one. From the day of our Founding, we have proclaimed that every man and woman on this earth has rights, and dignity, and matchless value, because they bear", 
         " the image of the Maker of Heaven and earth. Across the generations we have proclaimed the imperative of self-government, because no one is fit to be a master, and no one deserves to be a slave. Advancing these ideals", 
          "is the mission that created our Nation. It is the honorable achievement of our fathers. Now it is the urgent requirement of our nation's security, and the calling of our time.",
        "So it is the policy of the United States to seek and support the growth of democratic movements and institutions in every nation and culture, with the ultimate goal of ending tyranny in our world.",
        "This is not primarily the task of arms, though we will defend ourselves and our friends by force of arms when necessary. Freedom, by its nature, must be chosen, and defended by citizens, and sustained by the rule of ",
         " law and the protection of minorities. And when the soul of a nation finally speaks, the institutions that arise may reflect customs and traditions very different from our own. America will not impose our own style of", 
         " government on the unwilling. Our goal instead is to help others find their own voice, attain their own freedom, and make their own way.",
        "The great objective of ending tyranny is the concentrated work of generations. The difficulty of the task is no excuse for avoiding it. America's influence is not unlimited, but fortunately for the oppressed, America's", 
         " influence is considerable, and we will use it confidently in freedom's cause.",
        "My most solemn duty is to protect this nation and its people against further attacks and emerging threats. Some have unwisely chosen to test America's resolve, and have found it firm.",
        "We will persistently clarify the choice before every ruler and every nation: The moral choice between oppression, which is always wrong, and freedom, which is eternally right. America will not ",
        "  pretend that jailed dissidents prefer their chains, or that women welcome humiliation and servitude, or that any human being aspires to live at the mercy of bullies.",
        "We will encourage reform in other governments by making clear that success in our relations will require the decent treatment of their own people. America's belief in human dignity will guide our policies, ",
        "  yet rights must be more than the grudging concessions of dictators; they are secured by free dissent and the participation of the governed. In the long run, there is no justice without freedom, ",
        "  and there can be no human rights without human liberty.",
        "Some, I know, have questioned the global appeal of liberty —though this time in history, four decades defined by the swiftest advance of freedom ever seen, ",
        "  is an odd time for doubt. Americans, of all people, should never be surprised by the power of our ideals. Eventually, the call of freedom comes to every mind and every soul. ",
        "  We do not accept the existence of permanent tyranny because we do not accept the possibility of permanent slavery. Liberty will come to those who love it.",
        "Today, America speaks anew to the peoples of the world:",
        "All who live in tyranny and hopelessness can know: the United States will not ignore your oppression, or excuse your oppressors. When you stand for your liberty, we will stand with you.",
        "Democratic reformers facing repression, prison, or exile can know: America sees you for who you are: the future leaders of your free country.",
        "The rulers of outlaw regimes can know that we still believe as Abraham Lincoln did: Those who deny freedom to others deserve it not for themselves; and, under the rule of a just God, cannot long retain it.",
        "The leaders of governments with long habits of control need to know: To serve your people you must learn to trust them. Start on this journey of progress and justice, and America will walk at your side.",
        "And all the allies of the United States can know: we honor your friendship, we rely on your counsel, and we depend on your help. Division among free nations is a primary goal of freedom's enemies. ",
        "  The concerted effort of free nations to promote democracy is a prelude to our enemies' defeat.",
        "Today, I also speak anew to my fellow citizens:",
        "From all of you, I have asked patience in the hard task of securing America, which you have granted in good measure. Our country has accepted obligations that are difficult to fulfill,",
        "  and would be dishonorable to abandon. Yet because we have acted in the great liberating tradition of this nation, tens of millions have achieved their freedom. And as hope kindles hope, ",
        "  millions more will find it. By our efforts, we have lit a fire as well —a fire in the minds of men. It warms those who feel its power, it burns those who fight its progress, and one day this untamed ",
        "  fire of freedom will reach the darkest corners of our world.",
        "A few Americans have accepted the hardest duties in this cause —in the quiet work of intelligence and diplomacy ... the idealistic work of helping raise up free governments ... ",
        "  the dangerous and necessary work of fighting our enemies. Some have shown their devotion to our country in deaths that honored their whole lives —and we will always honor their names and their sacrifice.",
        "All Americans have witnessed this idealism, and some for the first time. I ask our youngest citizens to believe the evidence of your eyes. You have seen duty and allegiance in the determined faces of our soldiers. ",
        "  You have seen that life is fragile, and evil is real, and courage triumphs. Make the choice to serve in a cause larger than your wants, larger than yourself —and in your days you will add not just to ",
        "  the wealth of our country, but to its character.",
        "America has need of idealism and courage, because we have essential work at home —the unfinished work of American freedom. In a world moving toward liberty, ",
        "  we are determined to show the meaning and promise of liberty.",
        "In America's ideal of freedom, citizens find the dignity and security of economic independence, instead of laboring on the edge of subsistence. ",
        "  This is the broader definition of liberty that motivated the Homestead Act, the Social Security Act, and the G.I. Bill of Rights.",
        "  And now we will extend this vision by reforming great institutions to serve the needs of our time. To give every American a stake in the promise and future of our country,", 
        "  we will bring the highest standards to our schools, and build an ownership society. We will widen the ownership of homes and businesses, retirement savings and health insurance —preparing ",
        "  our people for the challenges of life in a free society. By making every citizen an agent of his or her own destiny, we will give our fellow Americans greater freedom from want and fear, ",
        "  and make our society more prosperous and just and equal.",
        "In America's ideal of freedom, the public interest depends on private character —on integrity, and tolerance toward others, and the rule of conscience in our own lives. ",
        "  Self-government relies, in the end, on the governing of the self. That edifice of character is built in families, supported by communities with standards, and sustained in our national ",
        "  life by the truths of Sinai, the Sermon on the Mount, the words of the Koran, and the varied faiths of our people. Americans move forward in every generation by reaffirming all that is ",
        "  good and true that came before —ideals of justice and conduct that are the same yesterday, today, and forever.",
        "In America's ideal of freedom, the exercise of rights is ennobled by service, and mercy, and a heart for the weak. Liberty for all does not mean independence from one another. Our nation relies",
        "  on men and women who look after a neighbor and surround the lost with love. Americans, at our best, value the life we see in one another, and must always remember that even the unwanted have worth.",
        "  And our country must abandon all the habits of racism, because we cannot carry the message of freedom and the baggage of bigotry at the same time.",
        "From the perspective of a single day, including this day of dedication, the issues and questions before our country are many. From the viewpoint of centuries, the questions that come to us are narrowed and few.",
        "  Did our generation advance the cause of freedom? And did our character bring credit to that cause?",
        "These questions that judge us also unite us, because Americans of every party and background, Americans by choice and by birth, are bound to one another in the cause of freedom. We have known divisions, ",
         " which must be healed to move forward in great purposes —and I will strive in good faith to heal them. Yet those divisions do not define America. We felt the unity and fellowship of our nation when freedom ",
        "  came under attack, and our response came like a single hand over a single heart. And we can feel that same unity and pride whenever America acts for good, and the victims of disaster are given hope, ",
        "  and the unjust encounter justice, and the captives are set free.",
        "We go forward with complete confidence in the eventual triumph of freedom. Not because history runs on the wheels of inevitability; it is human choices that move events. Not because we consider ourselves ",
        "  a chosen nation; God moves and chooses as He wills. We have confidence because freedom is the permanent hope of mankind, the hunger in dark places, the longing of the soul. When our Founders declared ",
        "  a new order of the ages; when soldiers died in wave upon wave for a union based on liberty; when citizens marched in peaceful outrage under the banner Freedom Now —they were acting on an ancient hope that ",
        "  is meant to be fulfilled. History has an ebb and flow of justice, but history also has a visible direction, set by liberty and the Author of Liberty.",
        "When the Declaration of Independence was first read in public and the Liberty Bell was sounded in celebration, a witness said, It rang as if it meant something. In our time it means something still. ",
        "  America, in this young century, proclaims liberty throughout all the world, and to all the inhabitants thereof. Renewed in our strength — tested, but not weary — we are ready for the greatest achievements ",
        "  in the history of freedom.",
        "May God bless you, and may He watch over the United States of America."]
    Bill_Clinton = [ 
        "At this last presidential inauguration of the 20th century, let us lift our eyes toward the challenges that await us in the next century. It is our great good fortune that time and chance have put us not only at the edge of a new century, in a new millennium, but on the edge of a bright new prospect in human affairs - a moment that will define our course, and our character, for decades to come. We must keep our old democracy forever young. Guided by the ancient vision of a promised land, let us set our sights upon a land of new promise.",
        "The promise of America was born in the 18th century out of the bold conviction that we are all created equal. It was extended and preserved in the 19th century, when our nation spread across the continent, saved the union, and abolished the awful scourge of slavery.",
        "Then, in turmoil and triumph, that promise exploded onto the world stage to make this the American Century.",
        "And what a century it has been. America became the world's mightiest industrial power; saved the world from tyranny in two world wars and a long cold war; and time and again, reached out across the globe to millions who, like us, longed for the blessings of liberty.",
        "Along the way, Americans produced a great middle class and security in old age; built unrivaled centers of learning and opened public schools to all; split the atom and explored the heavens; invented the computer and the microchip; and deepened the wellspring of justice by making a revolution in civil rights for African Americans and all minorities, and extending the circle of citizenship, opportunity and dignity to women.",
        "Now, for the third time, a new century is upon us, and another time to choose. We began the 19th century with a choice, to spread our nation from coast to coast. We began the 20th century with a choice, to harness the Industrial Revolution to our values of free enterprise, conservation, and human decency. Those choices made all the difference. At the dawn of the 21st century a free people must now choose to shape the forces of the Information Age and the global society, to unleash the limitless potential of all our people, and, yes, to form a more perfect union.",
        "When last we gathered, our march to this new future seemed less certain than it does today. We vowed then to set a clear course to renew our nation.",
        "In these four years, we have been touched by tragedy, exhilarated by challenge, strengthened by achievement. America stands alone as the world's indispensable nation. Once again, our economy is the strongest on Earth. Once again, we are building stronger families, thriving communities, better educational opportunities, a cleaner environment. Problems that once seemed destined to deepen now bend to our efforts: our streets are safer and record numbers of our fellow citizens have moved from welfare to work.",
        "And once again, we have resolved for our time a great debate over the role of government. Today we can declare: Government is not the problem, and government is not the solution. We - the American people - we are the solution. Our founders understood that well and gave us a democracy strong enough to endure for centuries, flexible enough to face our common challenges and advance our common dreams in each new day.",
        "As times change, so government must change. We need a new government for a new century - humble enough not to try to solve all our problems for us, but strong enough to give us the tools to solve our problems for ourselves; a government that is smaller, lives within its means, and does more with less. Yet where it can stand up for our values and interests in the world, and where it can give Americans the power to make a real difference in their everyday lives, government should do more, not less. The preeminent mission of our new government is to give all Americans an opportunity - not a guarantee, but a real opportunity - to build better lives.",
        "Beyond that, my fellow citizens, the future is up to us. Our founders taught us that the preservation of our liberty and our union depends upon responsible citizenship. And we need a new sense of responsibility for a new century. There is work to do, work that government alone cannot do: teaching children to read; hiring people off welfare rolls; coming out from behind locked doors and shuttered windows to help reclaim our streets from drugs and gangs and crime; taking time out of our own lives to serve others.",
        "Each and every one of us, in our own way, must assume personal responsibility - not only for ourselves and our families, but for our neighbors and our nation. Our greatest responsibility is to embrace a new spirit of community for a new century. For any one of us to succeed, we must succeed as one America.",
        "The challenge of our past remains the challenge of our future - will we be one nation, one people, with one common destiny, or not? Will we all come together, or come apart?",
        "The divide of race has been America's constant curse. And each new wave of immigrants gives new targets to old prejudices. Prejudice and contempt, cloaked in the pretense of religious or political conviction are no different. These forces have nearly destroyed our nation in the past. They plague us still. They fuel the fanaticism of terror. And they torment the lives of millions in fractured nations all around the world.",
        "These obsessions cripple both those who hate and, of course, those who are hated, robbing both of what they might become. We cannot, we will not, succumb to the dark impulses that lurk in the far regions of the soul everywhere. We shall overcome them. And we shall replace them with the generous spirit of a people who feel at home with one another.",
        "Our rich texture of racial, religious and political diversity will be a Godsend in the 21st century. Great rewards will come to those who can live together, learn together, work together, forge new ties that bind together.",
        "As this new era approaches we can already see its broad outlines. Ten years ago, the Internet was the mystical province of physicists; today, it is a commonplace encyclopedia for millions of schoolchildren. Scientists now are decoding the blueprint of human life. Cures for our most feared illnesses seem close at hand.",
        "The world is no longer divided into two hostile camps. Instead, now we are building bonds with nations that once were our adversaries. Growing connections of commerce and culture give us a chance to lift the fortunes and spirits of people the world over. And for the very first time in all of history, more people on this planet live under democracy than dictatorship.",
        "My fellow Americans, as we look back at this remarkable century, we may ask, can we hope not just to follow, but even to surpass the achievements of the 20th century in America and to avoid the awful bloodshed that stained its legacy? To that question, every American here and every American in our land today must answer a resounding Yes.",
        "This is the heart of our task. With a new vision of government, a new sense of responsibility, a new spirit of community, we will sustain America's journey. The promise we sought in a new land we will find again in a land of new promise.",
        "In this new land, education will be every citizen's most prized possession. Our schools will have the highest standards in the world, igniting the spark of possibility in the eyes of every girl and every boy. And the doors of higher education will be open to all. The knowledge and power of the Information Age will be within reach not just of the few, but of every classroom, every library, every child. Parents and children will have time not only to work, but to read and play together. And the plans they make at their kitchen table will be those of a better home, a better job, the certain chance to go to college.",
        "Our streets will echo again with the laughter of our children, because no one will try to shoot them or sell them drugs anymore. Everyone who can work, will work, with today's permanent under class part of tomorrow's growing middle class. New miracles of medicine at last will reach not only those who can claim care now, but the children and hardworking families too long denied.",
        "We will stand mighty for peace and freedom, and maintain a strong defense against terror and destruction. Our children will sleep free from the threat of nuclear, chemical or biological weapons. Ports and airports, farms and factories will thrive with trade and innovation and ideas. And the world's greatest democracy will lead a whole world of democracies.",
        "Our land of new promise will be a nation that meets its obligations - a nation that balances its budget, but never loses the balance of its values. A nation where our grandparents have secure retirement and health care, and their grandchildren know we have made the reforms necessary to sustain those benefits for their time. A nation that fortifies the world's most productive economy even as it protects the great natural bounty of our water, air, and majestic land.",
        "And in this land of new promise, we will have reformed our politics so that the voice of the people will always speak louder than the din of narrow interests - regaining the participation and deserving the trust of all Americans.",
        "Fellow citizens, let us build that America, a nation ever moving forward toward realizing the full potential of all its citizens. Prosperity and power - yes, they are important, and we must maintain them. But let us never forget: The greatest progress we have made, and the greatest progress we have yet to make, is in the human heart. In the end, all the world's wealth and a thousand armies are no match for the strength and decency of the human spirit.",
        "Thirty-four years ago, the man whose life we celebrate today spoke to us down there, at the other end of this Mall, in words that moved the conscience of a nation. Like a prophet of old, he told of his dream that one day America would rise up and treat all its citizens as equals before the law and in the heart. Martin Luther King's dream was the American Dream. His quest is our quest: the ceaseless striving to live out our true creed. Our history has been built on such dreams and labors. And by our dreams and labors we will redeem the promise of America in the 21st century.",
        "To that effort I pledge all my strength and every power of my office. I ask the members of Congress here to join in that pledge. The American people returned to office a President of one party and a Congress of another. Surely, they did not do this to advance the politics of petty bickering and extreme partisanship they plainly deplore. No, they call on us instead to be repairers of the breach, and to move on with America's mission.",
        "America demands and deserves big things from us - and nothing big ever came from being small. Let us remember the timeless wisdom of Cardinal Bernardin, when facing the end of his own life. He said: “It is wrong to waste the precious gift of time, on acrimony and division.",
        "Fellow citizens, we must not waste the precious gift of this time. For all of us are on that same journey of our lives, and our journey, too, will come to an end. But the journey of our America must go on.",
        "And so, my fellow Americans, we must be strong, for there is much to dare. The demands of our time are great and they are different. Let us meet them with faith and courage, with patience and a grateful and happy heart. Let us shape the hope of this day into the noblest chapter in our history. Yes, let us build our bridge. A bridge wide enough and strong enough for every American to cross over to a blessed land of new promise.",
        "May those generations whose faces we cannot yet see, whose names we may never know, say of us here that we led our beloved land into a new century with the American Dream alive for all her children; with the American promise of a more perfect union a reality for all her people; with America's bright flame of freedom spreading throughout all the world.",
        "From the height of this place and the summit of this century, let us go forth. May God strengthen our hands for the good work ahead - and always, always bless our America."
    ]
    
    bsh=[]
    
    clin=[]
    
    for i in range(0, len(Bush)):
        for j in range(0, len(Bush[i].split())):
            bsh.append(Bush[i].split()[j])
    for i in range(0, len(Bill_Clinton)):
        for j in range(0, len(Bill_Clinton[i].split())):
            clin.append(Bill_Clinton[i].split()[j])
    
    d=dict()
    e=dict()
    for c in bsh:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    
    for c in clin:
        if c not in e:
            e[c]=1
        else:
            e[c]=e[c]+1
    
    f=set()
    g=set()    
    for n in d:
        f.add(d[n])
    for n in e:
        g.add(e[n])
    
    bb=list(f)
    cc=list(g)
    
    print "George. Bush - "
    for m in d:
        if(d[m]>bb[len(bb)-10]):
            print "==", m, " : ", d[m],
    print"\n"
    print "Bill. Clinton -"
    for m in e:
        if(e[m]>cc[len(cc)-10]):
            print "==", m, " : ", e[m],
  
    
def lab11():

    ring()   
    addkeys()
    addmouse()
    turtle.listen()
    turtle.mainloop()
    schoolLife()
    speech()
    

def main():
     lab11()

if __name__=="__main__":
     main()
