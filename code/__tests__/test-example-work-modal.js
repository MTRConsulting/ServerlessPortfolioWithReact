// TODO: Remove this `raf` polyfill once the below issue is sorted
// https://github.com/facebookincubator/create-react-app/issues/3199#issuecomment-332842582
import raf from '../tempPolyfills'

import React from 'react'
import Enzyme from 'enzyme'
import Adapter from 'enzyme-adapter-react-16'
import { shallow } from 'enzyme'
import ExampleWorkModal from '../js/example-work-modal'

Enzyme.configure({ adapter: new Adapter() })

const myExample = {
  'title': 'Work Example',
  'href': 'https://example.com',
  'desc': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
  'image': {
    'desc': 'example screenshot of a project involving code',
    'src': 'images/example1.png',
    'comment': ''
  }
}

describe('ExampleWorkModal component', () => {
  let mockCloseModalFn = jest.fn()
  let closedComponent = shallow(<ExampleWorkModal example={myExample} open={false} />)
  let openComponent = shallow(<ExampleWorkModal example={myExample} open={true} closeModal={mockCloseModalFn} />)

  let anchors = closedComponent.find('a')
  let paragraph = closedComponent.find('p')

  console.log(closedComponent.debug())
  console.log(anchors.debug())
  console.log(paragraph.debug())

  it("Should contain a single 'a' element", () => {
    expect(anchors.length).toEqual(1)
  })

  it("Should link to our project", () => {
      expect(anchors.prop('href')).toEqual(myExample.href)
//    expect(anchors.node.props.href).toEqual(myExample.href)
  })

  it("Should have a description", () => {
    expect(paragraph.text()).toEqual(myExample.desc)
  })

  it("Should have the modal class set correctly closed", () => {
    expect(closedComponent.find(".background--skyBlue").hasClass("modal--closed")).toBe(true)
  })

  it("Should have the modal class set correctly opened", () => {
    expect(openComponent.find(".background--skyBlue").hasClass("modal--open")).toBe(true)
  })

  console.log(openComponent.debug())
  it("Should call the closeModal handler when clicked", () => {
    openComponent.find(".modal__closeButton").simulate('click')
    expect(mockCloseModalFn).toHaveBeenCalled()
  })
})
