lua_hero = """
    function main(splash, args)
        splash:set_viewport_size(1500, 2000)
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
            sel = string.format('label[data-id=%s]', key)
            click_btn(sel)
            splash:wait(args.wait/3)
            result[value] = splash:html()
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
                    new_dic[kind_value] = splash:html()  
                end
            end
            result[value['type']] = new_dic
        end 
        return result
    end
"""

lua_skill = """
    function main(splash, args)
        splash:set_viewport_size(1200, 2000)
        splash.images_enabled = false
        splash:autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash:go(args.url)
        splash:wait(args.wait)
        click_btn = splash:jsfunc([[
            function(btn_sel){
                $(btn_sel).click();
            }
        ]])
        get_infor = splash:jsfunc([[
             function(dic){
                dic['small_img'] = $('#spellDefail img:eq(0)').attr('src');
                dic['big_img'] = $('#spellDefail img:eq(1)').attr('src');
                dic['level'] = $('#spellDefail span:eq(0)').text();
                dic['des'] = $('.spell-desc').text();
            }
        ]])
        result = {model_name=args.model_name}
        for index, skill in pairs(args.skill_dic) do
            sel = string.format('img[alt=%s]', skill)
            click_btn(sel)
            splash:wait(args.wait)
            dic = {}
            get_infor(dic)
            splash:wait(args.wait)
            result[skill] = dic
        end
        return result
    end
"""

lua_skill1 = """
    function main(splash, args)
        splash:set_viewport_size(1500, 3000)
        splash.images_enabled = false
        splash:autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash:go(args.url)
        splash:wait(args.wait/2)
        click_btn = splash:jsfunc([[
            function(btn_sel){
                $(btn_sel).click();
            }
        ]])
        result = {model_name=args.model_name}
        for n, skill in pairs(args.skill_dic) do
            sel = string.format('img[alt=%s]', skill)
            click_btn(sel)
            splash:wait(args.wait/2)
            result[skill] = splash:html()
        end
        return result
    end
"""
