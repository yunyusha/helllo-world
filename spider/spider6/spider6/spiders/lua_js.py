

# 定义lua语法,模拟用户在英雄页面的点击操作
luo_hero = """
    function main(splash, args)
        splash: set_viewport_size(1200,2000)
        splash: go(args.url)
        splash:autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash: wait(args.wait)
        click_btn = splash:jsfunc([[
            function(btn_sel){
                $(btn_sel).click();
            }
        ]])
        result = {model_name=args.model_name}
        for key,value in pairs(args.kind_dic) do
            sel = string.format('label[data-id="%s"]', key)
            click_btn(sel)
            splash:wait(args.wait/2)
            result[value] = splash:html()
        end
        return result
    end

"""

lua_res1 = """
    function main(splash, args)
        splash: set_viewport_size(1200,3000)
        splash: go(args.url)
        splash.images_enabled = false
        splash: autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash: wait(args.wait)
        click_btn = splash: jsfunc([[
            function(btn_sel){
                $(btn_sel).click();
            }
        ]])
        result = {}
        for key, value in pairs(args.kind_dic) do
                sel_1 = string.format('li[data-item="%s"]>span',key)
                click_btn(sel_1)
                splash: wait(args.wait/2)
            for key_2, value_2 in pairs(value) do
                sel_2 = string.format('li[data-item="%s"]>span',value_2)
                click_btn(sel_2)
                splash: wait(args.wait/3)
                result[key_2] = splash:html()
            end
        end   
        return result
    end
    
"""
lua_res = """
    function main(splash, args)
        splash: set_viewport_size(1200,3000)
        splash.images_enabled = false
        splash: go(args.url)
        splash: autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash: wait(args.wait)
        click_btn = splash: jsfunc([[
            function(btn_sel){
                $(btn_sel).click();
            }
        ]])
        result = {}
        for key, value in pairs(args.kind_dic) do
                sel_1 = string.format('li[data-item="%s"]>span',key)
                click_btn(sel_1)
                splash: wait(args.wait/2)
            new_dic = {}
            for key_2, value_2 in pairs(value) do
                sel_2 = string.format('li[data-item="%s"]>span',value_2)
                click_btn(sel_2)
                splash: wait(args.wait/3)
                new_dic[key_2] = splash:png()
            end
            result[key] = new_dic
        end   
        return result
    end

"""

lua_shop = """
    function main(splash, args)
        splash:set_viewport_size(1500, 3000)
        splash.images_enabled = false
        splash:autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash:go(args.url)
        splash:wait(args.wait)
        click_btn = splash:jsfunc([[
            function(btn_sel){
                $(btn_sel).click();
            }
        ]])
        result = {model_name=args.model_name}
        for key, value in pairs(args.kind_dic) do
            sel = string.format('li[data-item=%s]>span', key)
            click_btn(sel)
            splash:wait(args.wait/3)
            new_dic = {}
            for kind_key, kind_value in pairs(value) do
                if(kind_key ~= "type")
                then
                    sel = string.format('li[data-item=%s]>span', kind_key)
                    click_btn(sel)
                    splash:wait(args.wait/3)
                    new_dic[kind_value] = splash:png()  
                end
            end
            result[value['type']] = new_dic
        end 
        return result
    end
"""
