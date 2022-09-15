import paddlehub as hub


module = hub.Module(name="ernie_vilg")
results = module.generate_image(text_prompts=["星际舰队，巨大黑洞，蒸汽波"])

