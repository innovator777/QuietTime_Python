#-*- coding:utf-8 -*-

import kw


def getMain():
  return {
    'message': {
      'text': '처음으로'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getTodaysQTMainTitle()]
    }
  }

def getQTChoice():
  return {
    'message': {
      'text': '항목을 선택해주세요.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getLLQTMainTitle(), kw.getDBQTMainTitle(), kw.getHome()]
    }
  }

def getLLQTChoice():
  return {
    'message': {
      'text': '항목을 선택해주세요.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getLLQTSubTitle(), kw.getLLQTCommentary(), kw.getHome()]
    }
  }

def getDBQTChoice():
  return {
    'message': {
      'text': '항목을 선택해주세요.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getDBQTMainTitle(), kw.getHome()]
    }
  }

def getUnappliedUserCase():
  return {
    'message': {
      'text': '서비스를 이용하기 위해서는 서비스 사용 신청을 진행해 주시기 바랍니다.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getApply(), kw.getHome()]
    }
  }
def getApplyManual():
  return {
    'message': {
      'text': '이름/년생/성별을 입력해주세요. \n' +
              '예시 => 홍길동/99년생/남성 \n\n'
    },
    'keyboard': {
      'type': 'text'
    }
  }

def getApplyQuietTime():
  return {
    'message': {
      'text': '감사합니다. 관리자의 확인 작업 이후부터 서비스 사용이 가능해집니다.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getHome()]
    }
  }

def getDisapprovedUserCase():
  return {
    'message': {
      'text': '관리자의 확인이 되지 않은 상태입니다.\n' +
              '관리자의 확인 작업 이후부터 서비스 사용이 가능해집니다.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getHome()]
    }
  }

def getLLQT(text):
  if getDataIsNoneDistinction(text):
    return {
      'message': {
        'text': '오늘의 큐티가 없습니다.\n' +
                '매일 12시 2~3분부터 이용 가능합니다. \n' +
                '이용에 문제가 있는경우 관리자에게 연락바랍니다.'
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getLLQTSubTitle(), kw.getLLQTCommentary(), kw.getHome()]
      }
    }
  else :
    return {
      'message': {
        'text': text
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getLLQTSubTitle(), kw.getLLQTCommentary(), kw.getHome()]
      }
    }

def getDBQT(text):
  if getDataIsNoneDistinction(text):
    return {
      'message': {
        'text': '오늘의 큐티가 없습니다.\n' +
                '매일 12시 2~3분부터 이용 가능합니다. \n' +
                '이용에 문제가 있는경우 관리자에게 연락바랍니다.'
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getDBQTMainTitle(), kw.getHome()]
      }
    }
  else :
    return {
      'message': {
        'text': text
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getDBQTMainTitle(), kw.getHome()]
      }
    }

def getAdmin():
  return {
    'message': {
      'text': u'관리자로 확인되었습니다.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getLLQTMainTitle(), kw.getDBQTMainTitle(), kw.getAdminFunction(), kw.getHome()]
    }
  }

def getAdminMode():
  return {
    'message': {
      'text': u'관리자 모드입니다.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getWaitList(), kw.getChangeUserState(), kw.getApproveList(), kw.getHome()]
    }
  }


def getUserStateChangeMode():
  return {
    'message': {
      'text' : u'유저키를 입력해주세요.'
    },
    'keyboard': {
      'type': 'text'
    }
  }

def getUserStateChangeResult(text):
  return {
    'message': {
      'text' : text
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getTodaysQTMainTitle()]
    }
  }

def getEnterIncorrectlyWord():
  return {
    'message': {
      'text' : u'잘못 입력하셨습니다.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getWaitList(), kw.getChangeUserState(), kw.getApproveList(), kw.getHome()]
    }
  }

def getWrongAccess():
  return {
    'message': {
      'text' : u'잘못된 접근입니다. \n' +
                '처음으로 돌아갑니다.'
    },
    'keyboard': {
      'type': 'buttons',
      'buttons': [kw.getTodaysQTMainTitle()]
    }
  }

def getWaitUserList(text):
  if getDataIsNoneDistinction(text):
    return {
      'message': {
        'text': u'대기 유저가 없습니다.'
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getWaitList(), kw.getChangeUserState(), kw.getApproveList(), kw.getHome()]
      }
    }
  else:
    return {
      'message': {
        'text': text
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getWaitList(), kw.getChangeUserState(), kw.getApproveList(), kw.getHome()]
      }
    }

def getApproveUserList(text):
  if getDataIsNoneDistinction(text):
    return {
      'message': {
        'text': u'사용중인 유저가 없습니다.'
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getWaitList(), kw.getChangeUserState(), kw.getApproveList(), kw.getHome()]
      }
    }
  else:
    return {
      'message': {
        'text': text
      },
      'keyboard': {
        'type': 'buttons',
        'buttons': [kw.getWaitList(), kw.getChangeUserState(), kw.getApproveList(), kw.getHome()]
      }
    }

def getDataIsNoneDistinction(data):
  if data is None:
    return True
  else:
    return False
