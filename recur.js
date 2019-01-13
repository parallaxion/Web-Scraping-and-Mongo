
level = 0
function findStuff(someDict) {
    for (x in someDict) {

        if ((typeof someDict[x]) == 'object'){

            level = level + 1
            var str = new Array(level).join('.');
            console.log(str + x + " (" + typeof someDict[x] +")")
           
            findStuff(someDict[x])
            level = level -1
        }
        else{
            
            var str = new Array(level).join('.');
            console.log(str + someDict[x])
        }
    }

}

bla = {"any complex data structure": {"traits":["guy",{"5'11\"":["blonde","blue"]}]}, "duplicate":{"traits":[[1,2,3,4,5,2136666,43,`0000`,3,2,2,2],"cool"]}}
findStuff(bla)