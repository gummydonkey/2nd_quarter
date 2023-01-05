""" Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

x = int(input())
y = int(input())


function(allstates,arg1,arg2,_,_,_,_,_,_,_,_,_,TableIndex)
    if not aura_env.config.enable then return end
    if arg1 == "CHAT_MSG_LOOT" and arg2 ~= nil then 
        
        local format ,mtfl= string.format,math.floor
        local strs,strf = string.sub,string.find
        local tnmbr = tonumber
        
        
        
        local it, _ = string.find(arg2, "%|c")
        local _, nk = string.find(arg2, "%]%|h%|r")
        local link = string.sub(arg2, it, nk)
        
        local itemid = tnmbr(link:match("item:(%d+):"))
        local block = false
        
        local _,_,iquality,_,_,_,_,_,_,itemIcon = GetItemInfo(itemid)
        
        local q = tonumber(iquality)+1
        if  aura_env.config.quality[q] then
            block = true
        end
        
        local i = 1
        while aura_env.config.ignore[i] do            
            if aura_env.config.ignore[i].item == itemid then
                block = true
                break
            end
            i = i + 1
            
        end
        
        i = 1
        while aura_env.config.nignore[i] do            
            if aura_env.config.nignore[i].nitem == itemid then
                block = false
                break
            end
            i = i + 1
            
        end
        
        if block then
            return
        end
        
        local who
        
        
        local wh,_ = strf(arg2, "добыча")
        if wh then
            who = strs(arg2, 1, wh-2)
            if who == "Ваша" then
                who,_ = UnitName("player")
                
                
            end
        else
            wh,_ = strf(arg2, "получа")
            if wh then 
                who = strs(arg2, 1, wh-2)
                if who == "Вы" then
                    who,_ = UnitName("player")
                    
                end
            else
                wh,_ = strf(arg2, "созда")
                if wh then
                    
                    who = strs(arg2, 1, wh-2)
                    if who == "Вы" then
                        who,_ = UnitName("player")
                        -- print(who)
                    end
                else
                    wh,_ = strf(arg2, "выигрыв")
                    if wh then                        
                        who = strs(arg2, 1, wh-2)
                        if who == "Вы" then
                            who,_ = UnitName("player")
                            -- print(who)
                        end
                    else
                        return
                    end
                end
            end
            endfunction()
            
            return
            endfunction(allstates, event, ...)
            allstates[""] = {
                show = true,
                changed = true,
                progressType = "static"|"timed",
                value = ,
                total = ,
                duration = ,
                expirationTime = ,
                autoHide = true,
                name = ,
                icon = ,
                stacks = ,
                index = ,
            }
            return true
        end
        if who == aura_env.MyName and not aura_env.config.selfloot then return end
        if who ~= aura_env.MyName and not aura_env.config.nselfloot then return end
        
        local r,g,b
        
        local kolvo
        local ko,lvo = strf(arg2, "x%d.")
        if ko then
            kolvo = tnmbr(strs(arg2, ko+1, lvo-1))
        else
            if aura_env.group == false then
                
                kolvo = 1
                
            else
                kolvo = 1
            end
            
        end
        --print(kolvo)
        local class
        i = 1
        while UnitExists("party"..i) do
            local name = UnitName("party"..i)
            if who == name then
                local _,class =  UnitClass("party"..i)
                r,g,b = GetClassColor(class)
                break
            else
                i = i + 1
            end
        end
        i = 1
        while UnitExists("raid"..i) do
            local name = UnitName("raid"..i)
            if who == name then
                local _,class =  UnitClass("raid"..i)
                r,g,b = GetClassColor(class)
                break
            end
            i = i + 1
            
        end
        if not r then
            local _,class =  UnitClass("player")
            r,g,b = GetClassColor(class)
        end
        
        local hex = format("%02x%02x%02x", mtfl(255 * r), mtfl(255 * g), mtfl(255 * b))
        
        if not who then return end
        if aura_env.config.group == false then
            allstates[TableIndex] = {
                show = true,
                changed = true,
                progressType = "timed",
                duration = aura_env.config.duration,
                expirationTime = GetTime() + aura_env.config.duration,
                autoHide = true,
                link = link,
                name = "|cff"..hex..who.."|r",
                icon = itemIcon,
                
                itemId = itemid,
                kolvo = "x"..kolvo,
                
                
            }
            return true
        else
            aura_env.HistoryTable[itemid] = aura_env.HistoryTable[itemid] or {}
            aura_env.HistoryTable[itemid][who] = (aura_env.HistoryTable[itemid][who] or 0) + kolvo
            
            allstates[itemid] = {
                show = true,
                changed = true,
                progressType = "timed",
                duration = aura_env.config.hduration,
                expirationTime = GetTime() + aura_env.config.hduration,
                autoHide = true,
                link = link,
                name = "|cff"..hex..who.."|r",
                icon = itemIcon,
                
                itemId = itemid,
                kolvo = "x"..aura_env.HistoryTable[itemid][who]
                
            }
            return true
        end
        
        
        
        
    end
end

duration