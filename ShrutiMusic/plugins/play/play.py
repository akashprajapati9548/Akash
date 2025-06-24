import os # Import os module at the top of the file if not already there

# ... (baaki code wahi rahega) ...

    if audio_telegram:
        if audio_telegram.file_size > 104857600:
            return await mystic.edit_text(_["play_5"])
        duration_min = seconds_to_min(audio_telegram.duration)
        if (audio_telegram.duration) > config.DURATION_LIMIT:
            return await mystic.edit_text(
                _["play_6"].format(config.DURATION_LIMIT_MIN, app.mention)
            )
        file_path = await Telegram.get_filepath(audio=audio_telegram)
        
        # ***** Yahan Naya Code Add Karo *****
        download_success = await Telegram.download(_, message, mystic, file_path)
        
        if not download_success:
            return await mystic.edit_text("Failed to download the file. Please try again.")

        if not os.path.exists(file_path):
            # Agar download success hua, par file exist nahi karti
            print(f"DEBUG: File not found on disk after successful download reported: {file_path}")
            return await mystic.edit_text("Error: Downloaded file is missing on the server. Please report this issue.")
        # ***********************************

        # Agar file_path exists karta hai, tabhi aage badho
        if os.path.exists(file_path): # Yeh condition ab zaroori ho jayegi
            message_link = await Telegram.get_link(message)
            file_name = await Telegram.get_filename(audio_telegram, audio=True)
            dur = await Telegram.get_duration(audio_telegram, file_path)
            details = {
                "title": file_name,
                "link": message_link,
                "path": file_path,
                "dur": dur,
            }

            try:
                await stream(
                    _,
                    mystic,
                    user_id,
                    details,
                    chat_id,
                    user_name,
                    message.chat.id,
                    streamtype="telegram",
                    forceplay=fplay,
                )
            except Exception as e:
                print(f"Error during streaming: {e}") # Yahan par "Error:" message change kiya hai
                ex_type = type(e).name
                err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
                return await mystic.edit_text(err)
            return await mystic.delete()
        else:
            # Ye else case tab aayega jab os.path.exists(file_path) fail hoga directly
            # Upar ka check already isko handle karega, but for redundancy.
            return await mystic.edit_text("Error: Could not find the file for streaming.")
    return # Yeh ensure karta hai ki agar audio_telegram nahi hai toh function end ho jaye
