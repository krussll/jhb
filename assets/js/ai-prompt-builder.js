(function () {
  'use strict'

  var STRUGGLE_CONFIG = {
    weight: {
      phrase: 'dropping short or heavy on draw shots (weight control), especially when jack lengths change between ends',
      faultDesc: 'my draw bowls are consistently finishing 2 to 3 feet short of the jack or running heavy through the head when the green speed changes',
      tacticsFocus: 'judging weight adjustments on changing jack lengths and protecting head position',
      recTitle: 'Ultimate Guide to Weight Control in Lawn Bowls:',
      recDesc: 'Learn the pendulum swing and stance adjustments to stop dropping short on changing green speeds.',
      recPath: '/help/ultimate-guide-to-weight-control',
    },
    line: {
      phrase: 'missing narrow or wide of my aiming point (line and bias control)',
      faultDesc: 'I am struggling to hold a consistent delivery line—either turning the bowl narrow inside the line or pushing it wide past the head',
      tacticsFocus: 'choosing the wide vs. narrow hand and using clear rink aiming points',
      recTitle: 'Line and Length in Lawn Bowls:',
      recDesc: 'Master shoulder aiming points, anchor foot alignment, and green reading for pinpoint draw lines.',
      recPath: '/help/line-and-length-in-lawn-bowls-how-to-win-at-bowls',
    },
    dumping: {
      phrase: 'smoothing out my release so I stop bouncing or dumping the bowl onto the turf',
      faultDesc: 'my bowl bounces or dumps loudly onto the green on release, losing 2 to 3 yards of weight and wobbling off line',
      tacticsFocus: 'maintaining a calm, low release under scoreboard pressure',
      recTitle: 'How to Stop Dumping Your Lawn Bowl:',
      recDesc: 'Fix early release, stiff back-knee bend, and grip tension with our step-by-step biomechanical guide.',
      recPath: '/help/how-do-i-stop-my-lawn-bowl-from-dumping',
    },
    hands: {
      phrase: 'closing the accuracy gap between my forehand draw and my backhand draw',
      faultDesc: 'I feel comfortable on my favourite hand, but my body alignment and release feel awkward when forced onto the opposite hand',
      tacticsFocus: 'deciding when to switch hands to attack the jack or avoid blockers',
      recTitle: 'How to Film & Analyse Your Lawn Bowls Delivery:',
      recDesc: 'Use a 2-angle smartphone video audit to spot why your alignment shifts between forehand and backhand.',
      recPath: '/ai/how-to-film-and-analyse-your-lawn-bowls-delivery',
    },
    weighted: {
      phrase: 'playing controlled weight, wresting out shot bowls, and trailing the jack without losing my line',
      faultDesc: 'when I add extra weight for a rest, trail, or conversion shot, I snatch my backswing and miss the target line wide or narrow',
      tacticsFocus: 'weighing up percentage draw shots against controlled weight or firing shots',
      recTitle: '5 Common Lawn Bowls Delivery Faults & Fixes:',
      recDesc: 'See how to add pace smoothly through your stride and pendulum swing without snatching at the wood.',
      recPath: '/help/5-common-lawn-bowls-delivery-faults',
    },
    tactics: {
      phrase: 'reading the head, building cover behind the jack, and calling high-percentage shots',
      faultDesc: 'I can bowl a reasonable draw in practice, but in competitive matches I lose shots by playing the wrong call for the state of the head',
      tacticsFocus: 'building and protecting the head, managing scoreboard pressure, and calling percentage shots',
      recTitle: 'Ultimate Guide to Lawn Bowls Singles & Head Tactics:',
      recDesc: 'Learn how to build the head, place positional back bowls, and control momentum end after end.',
      recPath: '/help/ultimate-guide-to-lawn-bowls-singles-tactics',
    },
  }

  function buildPromptText(mode, position, surface, struggleKey, duration) {
    var cfg = STRUGGLE_CONFIG[struggleKey] || STRUGGLE_CONFIG.weight

    if (mode === 'tactics') {
      return (
        'Act as an experienced lawn bowls tactical coach. Let\'s play an interactive 5-end tactical scenario simulator tailored for a ' +
        position +
        ' playing on a ' +
        surface +
        ' with a focus on ' +
        cfg.tacticsFocus +
        '. Present me with 5 realistic match situations one at a time (include the current score, end number, jack length, where my bowls and the opposition\'s bowls sit relative to the jack and ditch, and how many bowls remain). Wait for me to reply with the shot I would play and why, then critique my decision using percentage lawn bowls tactics before giving me the next scenario.'
      )
    }

    if (mode === 'fault') {
      return (
        'Act as a lawn bowls biomechanics and delivery coach. I play ' +
        position +
        ' on a ' +
        surface +
        '. Right now, here is what is happening on the mat: ' +
        cfg.faultDesc +
        '. Ask me 5 specific diagnostic questions about my grip pressure, anchor foot alignment, knee bend, step-to-swing timing, and release height to isolate the mechanical root cause. Then give me 2 simple physical feel cues and a 20-bowl corrective drill I can run in a ' +
        duration +
        ' practice session.'
      )
    }

    return (
      'Act as a qualified lawn bowls coach. I play ' +
      position +
      ' on a ' +
      surface +
      '. Right now, my biggest focus is ' +
      cfg.phrase +
      '. Design a structured ' +
      duration +
      ' solo roll-up session split into 3 scored drills using 4 bowls, 1 jack, and 2 markers. Include clear setup instructions, a target score out of 20 for each drill so I can track my progress, and 2 physical feel cues for my delivery.'
    )
  }

  function initBuilder(container) {
    var baseurl = container.getAttribute('data-baseurl') || ''
    var form = container.querySelector('[data-ai-form]')
    var positionSelect = container.querySelector('[data-ai-position]')
    var surfaceSelect = container.querySelector('[data-ai-surface]')
    var struggleSelect = container.querySelector('[data-ai-struggle]')
    var durationSelect = container.querySelector('[data-ai-duration]')
    var outputTextarea = container.querySelector('[data-ai-output]')
    var copyBtn = container.querySelector('[data-ai-copy-btn]')
    var copyLabel = container.querySelector('[data-ai-copy-label]')
    var copyStatus = container.querySelector('[data-ai-copy-status]')
    var chatgptLink = container.querySelector('[data-ai-chatgpt-link]')
    var recTitle = container.querySelector('[data-ai-rec-title]')
    var recDesc = container.querySelector('[data-ai-rec-desc]')
    var recLink = container.querySelector('[data-ai-rec-link]')

    if (!form || !outputTextarea) {
      return
    }

    function getSelectedMode() {
      var checked = container.querySelector('input[name="ai_mode"]:checked')
      return checked ? checked.value : 'rollup'
    }

    function updateChatgptHref(text) {
      if (chatgptLink) {
        chatgptLink.setAttribute(
          'href',
          'https://chatgpt.com/?q=' + encodeURIComponent(text)
        )
      }
    }

    function updateRecommendation(struggleKey) {
      var cfg = STRUGGLE_CONFIG[struggleKey] || STRUGGLE_CONFIG.weight
      if (recTitle) {
        recTitle.textContent = cfg.recTitle + ' '
      }
      if (recDesc) {
        recDesc.textContent = cfg.recDesc + ' '
      }
      if (recLink) {
        var cleanPath = (baseurl + cfg.recPath).replace('//', '/')
        recLink.setAttribute('href', cleanPath)
      }
    }

    function refreshPrompt() {
      var mode = getSelectedMode()
      var position = positionSelect ? positionSelect.value : 'Lead'
      var surface = surfaceSelect
        ? surfaceSelect.value
        : 'medium outdoor grass green (13–15 seconds)'
      var struggleKey = struggleSelect ? struggleSelect.value : 'weight'
      var duration = durationSelect ? durationSelect.value : '45-minute'

      var promptText = buildPromptText(
        mode,
        position,
        surface,
        struggleKey,
        duration
      )
      outputTextarea.value = promptText
      updateChatgptHref(promptText)
      updateRecommendation(struggleKey)
    }

    form.addEventListener('change', refreshPrompt)

    outputTextarea.addEventListener('input', function () {
      updateChatgptHref(outputTextarea.value)
    })

    form.addEventListener('submit', function (event) {
      event.preventDefault()
      var textToCopy = outputTextarea.value

      function showCopiedFeedback() {
        if (copyStatus) {
          copyStatus.textContent = 'Copied! Paste into ChatGPT, Claude, or Gemini.'
        }
        if (copyLabel) {
          copyLabel.textContent = 'Copied to Clipboard!'
        }
        setTimeout(function () {
          if (copyLabel) {
            copyLabel.textContent = 'Copy Prompt to Clipboard'
          }
        }, 3000)
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard
          .writeText(textToCopy)
          .then(showCopiedFeedback)
          .catch(function () {
            outputTextarea.select()
            document.execCommand('copy')
            showCopiedFeedback()
          })
      } else {
        outputTextarea.select()
        document.execCommand('copy')
        showCopiedFeedback()
      }
    })

    refreshPrompt()
  }

  document.addEventListener('DOMContentLoaded', function () {
    var builders = document.querySelectorAll('[data-ai-prompt-builder]')
    for (var i = 0; i < builders.length; i += 1) {
      initBuilder(builders[i])
    }
  })
})()
