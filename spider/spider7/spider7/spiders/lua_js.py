

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
            result[value] = splash:png()
        end
        return result
    end

"""

lua_res = """
    function main(splash, args)
        splash: set_viewport_size(1200,4000)
        splash: go(args.url)
        splash: autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash: wait(args.wait)
        click_btn = splash: jsfunc([[
            function(btn_sel){
                $(btn_sel).click();
            }
        ]])
        result = {model_name=args.model_name}
        for key, value in pairs(args.kind_dic) do
                sel_1 = string.format('li[data-item=%s]',key)
                click_btn(sel_1)
                splash: wait(args.wait/4)
            for key_2, value_2 in pairs(value) do
                sel_2 = string.format('li[data-item=%s]',value_2)
                splash: wait(args:wait/4)
            end
            
        return splash:png()
        
        end
        
        
        
"""