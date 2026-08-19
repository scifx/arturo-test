# ui 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `alert`

Documentation: https://arturo-lang.io/documentation/library/ui/alert

### Example 1

```arturo
alert "Hello!" "This is a notification..."
; show an OS notification without any styling

alert.error "Ooops!" "Something went wrong!"
; show an OS notification with an error message
```

## `clip`

Documentation: https://arturo-lang.io/documentation/library/ui/clip

### Example 1

```arturo
clip "this is something to be pasted into the clipboard"
```

## `dialog`

Documentation: https://arturo-lang.io/documentation/library/ui/dialog

### Example 1

```arturo
selectedFile: dialog "Select a file to open"
; gets full path for selected file, after dialog closes
```

### Example 2

```arturo
selectedFolder: dialog.folder "Select a folder"
; same as above, only for folder selection
```

## `popup`

Documentation: https://arturo-lang.io/documentation/library/ui/popup

### Example 1

```arturo
popup "Hello!" "This is a popup message"
; shows a message dialog with an OK button
; when the dialog is closed, it returns: true
```

### Example 2

```arturo
if popup.yesNo "Hmm..." "Are you sure you want to continue?" [
    ; a Yes/No dialog will appear - if the user clicks YES,
    ; then the function will return true; thus we can do what
    ; we want here

]
```

### Example 3

```arturo
popup.okCancel.literal "Hello" "Click on a button"
; => 'ok (if user clicked OK)
; => 'cancel (if user clicked Cancel)
```

## `unclip`

Documentation: https://arturo-lang.io/documentation/library/ui/unclip

### Example 1

```arturo
; paste something into the clipboard (optionally)
clip "this is something to be pasted into the clipboard"

; now, let's fetch whatever there is in the clipboard
unclip
; => "this is something to be pasted into the clipboard"
```

## `webview`

Documentation: https://arturo-lang.io/documentation/library/ui/webview

### Example 1

```arturo
webview "Hello world!"
        ; (opens a webview windows with "Hello world!")
```

### Example 2

```arturo
        webview .width:  200 
    .height: 300
    .title:  "My webview app"
        ; (opens a webview with given attributes)
        ---
<h1>This is my webpage</h1>
<p>
    This is some content
</p>
```
