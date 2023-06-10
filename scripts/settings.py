from modules import script_callbacks, shared

def on_ui_settings():
    shared.opts.add_option("eps_enable_save_raw_prompt_to_pnginfo", shared.OptionInfo(False, "单击 png图片信息 保存到", section=("easy_prompt_selector", "EasyPromptSelector")))
    shared.opts.add_option("eps_use_old_template_feature", shared.OptionInfo(False, "使用原随机功能实现（sdweb-eagle-pnginfo 的兼容性）", section=("easy_prompt_selector", "EasyPromptSelector")))

script_callbacks.on_ui_settings(on_ui_settings)
